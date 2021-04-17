from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from BMIcalcapp.models import BMI
from django.contrib.auth.decorators import login_required

@login_required
def bmi_data_entry(request):
    context = {'title': "Weight | Height | BMI"}
    return render(request, "form.html", context)

@login_required
def bmi_calculator(request):
    try: BMI =  round(float(request.GET['weight']) / (float(request.GET['height']))**2, 3)
    except: return HttpResponseRedirect(reverse('BMIcalculator:data_entry'))
	
    if 18.5 < BMI < 25: 
        message = f"Your BMI: {BMI} is in normal range, until now"
        result="normal"
    elif 25 <= BMI < 30: 
        message = f"Your BMI: {BMI} shows you're overweight, bring more exercise to your routine"
        result = "overweight"
    elif BMI <= 18.5: 
        message = f"Your BMI: {BMI} shows you're underweight, eat more nutritious food"
        result = "underweight"
    elif BMI >= 30:
        message = f"Your BMI: {BMI} shows your obesity level is high, consider going to gym."
        result = "obese"

    context = {'title':'YOUR BMI RESULT', 'result': result, 'BMI': BMI, "message":message}

    return render(request, 'result.html', context)



