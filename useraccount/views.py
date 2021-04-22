from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from useraccount.forms import CustomCreationForm, CustomUpdateForm
from django.contrib.auth.models import User
from  useraccount.models import UserModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random
from BMIcalcapp.views import save_data
from verify_email.email_handler import send_verification_email


def home(request):
    context = {'title':'Home'}
    return render(request, "home.html", context)

    
def login_view(request):
    form = AuthenticationForm(request.POST or None)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('BMIcalculator:data_entry'))
    context = {'form' : form}
    return render(request, "login.html", context)


def register_view(request):
    form = CustomCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        send_verification_email(request, form)

        return HttpResponseRedirect(reverse('user:login'))
    context = {'form':form, 'title':'Register Form'}
    return render(request, 'register.html', context)

@login_required        
def update_view(request):
    user = get_object_or_404(UserModel, user=request.user)
    form = CustomUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    context = {'form':form, 'title':'Update Form'}
    return render(request, 'register.html', context)
    

def logout_view(request):
   logout(request)
   return HttpResponseRedirect(reverse('home'))

# @login_required
# def send_confirmation(request):

#     current_user = UserModel.objects.filter(user=request.user)[0]
#     email =  current_user.email

#     if not current_user.email_confirmed:
#         code  = random.randint(100000, 999999)
#         subject = "Confirmation code"
#         message = 'Here is your secret confirmation code:'
#         from_email = 'bnodtwari3@gmail.com'
#         recipient_list = [
#             email,
#         ]
#         inner_context = {'code':code, 'user':request.user}
#         html_message = render_to_string('confirm_message.html', inner_context)
#         send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#         return render(request,'email_confirmation.html')
#     else:    
#         context = {'title':'CONFIRM EMAIL', "startswith": email[0:4]}
#         return render(request, 'email_confirmation', )
    
@login_required
def send_suggestions(request):
    save_data(request)

    current_user = User.objects.filter(id=request.user.id)[0]
    email =  current_user.email
    if current_user.is_active:
        BMI_value = request.POST['BMI_value']
        height = float(request.POST['height'])  
        weight = float(request.POST['weight'])
        result = request.POST.get('result')
        document = 'suggestions/' + result + ".html"

        if result=="normal": message = f"Your BMI: {BMI_value} is in normal range, until now"
        elif result=="overweight": message = f"Your BMI: {BMI_value} shows you're overweight, bring more exercise to your routine"
        elif result =="underweight": message = f"Your BMI: {BMI_value} shows you're underweight, eat more nutritious food"
        elif result=="obese":message = f"Your BMI: {BMI_value} shows your obesity level is high, consider going to gym."
        result = "obese"
        document = "suggestions/obese.html"

        subject = "Suggestions Page"
        from_email = 'bnodtwari1112@gmail.com'
        recipient_list = [
            email,
        ]
        context = {
            'title': result.title() + ' BMI and Suggestions',
               'result': result, 
               'BMI': BMI_value, 
               'message':message, 
               "height":height, 
               "weight":weight,
               "length_unit":request.POST['length_unit'],
               "weight_unit":request.POST['weight_unit']
               
        }
        html_message = render_to_string(document, context)
        send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=False)
        return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    
    return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    