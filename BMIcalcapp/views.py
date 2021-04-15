from django.shortcuts import render
from django.http import HttpResponse
from BMIcalcapp.models import BMI
from django.contrib.auth.decorators import login_required

@login_required
def bmi_data_entry(request):
    context = {'title': "Weight | Height | BMI"}
    return render(request, "form.html", context)

@login_required
def bmi_calculator(request):
    try: BMI =  round(float(request.GET['weight']) / (float(request.GET['height']))**2, 3)
    except: return HttpResponse("Please Enter Values Properly!")

    if 18.5 < BMI < 25: return HttpResponse(f"Your BMI: {BMI} is in normal range, until now")
    elif 25 <= BMI < 30: 
        return HttpResponse(f"Your BMI: {BMI} shows you're overweight, bring more exercise to your routine")
    elif BMI <= 18.5:
         return HttpResponse(f"Your BMI: {BMI} shows you're underweight, eat more nutritious food")    
    elif BMI >= 30: 
        return HttpResponse(f"Your BMI: {BMI} shows your obesity level is high, consider going to gym.")



