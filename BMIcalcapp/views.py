from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from BMIcalcapp.models import BMI
from django.contrib.auth.models import User
from useraccount.models import UserModel

@login_required
def bmi_data_entry(request):
    context = {'title': "Weight | Height | BMI"}
    return render(request, "form.html", context)



def meterify(request):
    height = float(request.GET['height'])
    unit = request.GET['length_unit'] 
    if unit == "centimeter": return round((height * 0.01), 2)
    elif unit == "foot" : return round((height * 0.3048), 2)
    elif unit == "inch" : return round((height * 0.0254), 2)
    else: return round(height, 2)


def kilofy(request):
    weight = float(request.GET['weight'])
    unit = request.GET['weight_unit']
    if unit == 'Pound': return round((weight *0.453592), 2)
    else: return round(weight, 2)


@login_required
def bmi_calculator(request):
    weight = kilofy(request)
    height = meterify(request)
    try: BMI =  round((weight / ((height)**2)), 2)
    except: return HttpResponseRedirect(reverse('BMIcalculator:data_entry'))
    
    if 18.5 < BMI < 25: 
        message = f"Your BMI: {BMI} is in normal range, until now"
        result="normal"
        document = "suggestions/normal.html"
    elif 25 <= BMI < 30: 
        message = f"Your BMI: {BMI} shows you're overweight, bring more exercise to your routine"
        result = "overweight"
        document = "suggestions/overweight.html"
    elif BMI <= 18.5: 
        message = f"Your BMI: {BMI} shows you're underweight, eat more nutritious food"
        result = "underweight"
        document = "suggestions/underweight.html"
    elif BMI >= 30:
        message = f"Your BMI: {BMI} shows your obesity level is high, consider going to gym."
        result = "obese"
        document = "suggestions/obese.html"
    context = {'title': result.title() + ' BMI and Suggestions',
               'result': result, 
               'BMI': BMI, 
               'message':message, 
               "height":height, 
               "weight":weight,
               "length_unit":request.GET['length_unit'],
               "weight_unit":request.GET['weight_unit']
               }
    return render(request, document, context)




@login_required
def save_data(request):
    # print(request.GET)
    BMI_value = request.POST['BMI_value']
    height = float(request.POST['height'])  
    weight = float(request.POST['weight'])
    # print("hey don't get confused", request.user, "id------", request.user.pk, (User.objects.filter(pk=2)))
    user = UserModel.objects.filter(user=request.user)[0]

    user.bmi = round(float(BMI_value), 2)
    user.height = round(float(height), 2)
    user.weight = round(float(weight), 2)
    user.save()

    return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))

@login_required
def delete_data(request):
    user = UserModel.objects.filter(user=request.user)[0]
    user.bmi = None
    user.height = None
    user.weight = None
    user.save()
    return HttpResponseRedirect(reverse('BMIcalculator:dashboard'))
    

@login_required
def dashboard(request):
    user = UserModel.objects.filter(user=request.user)[0]
    if not user.email:
        user.email = request.user.email
        user.save()
    return render(request, 'dashboard.html', context={'user':user, 'title':"DASHBOARD"})


