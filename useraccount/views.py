from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from useraccount.forms import CustomCreationForm, CustomUpdateForm, CustomLoginForm
from django.contrib.auth.models import User
from  useraccount.models import UserModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random
from BMIcalcapp.views import save_data, get_status
from verify_email.email_handler import send_verification_email


def home(request):
    context = {'title':'Home'}
    return render(request, "home.html", context)

    
def login_view(request):
    form = CustomLoginForm(request.POST or None)
  
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
    context = {'form':form, 'title':'Register'}
    return render(request, 'register.html', context)
    

def logout_view(request):
   if str(request.user) != "AnonymousUser":
       logout(request)
       return HttpResponseRedirect(reverse('home'))
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required        
def update_view(request):
    user = get_object_or_404(UserModel, user=request.user)
    form = CustomUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        # if user.email != request.POST.get('email'):
        #     send_verification_email(request, form)    
        form.save()
        return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    context = {'form':form, 'title':'Update'}
    return render(request, 'update.html', context)

@login_required
def send_suggestions(request):
    save_data(request)
    
    email =  request.user.email
    if request.user.is_active:
        BMI_value = float(request.POST['BMI_value'])
        height = float(request.POST['height'])  
        weight = float(request.POST['weight'])
        subject = "Suggestions Page"
        from_email = 'bnodtwari1112@gmail.com'
        recipient_list = [
            email,
        ]
        state =  get_status(BMI_value)
        result = state.state
        message = state.suggestions
        document = f"suggestions/{result}.html"

        context = {'title': result.title() + ' BMI and Suggestions',
               'result': result, 
               'BMI': BMI_value, 
               'message':message, 
               "height":height, 
               "weight":weight,
               "length_unit":height,
               "weight_unit":weight,
               }
        html_message = render_to_string(document, context)
        send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=False)
        return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    
    return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))



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
        