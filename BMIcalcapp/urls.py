from django.urls import path
from BMIcalcapp.views import bmi_calculator, bmi_data_entry

app_name = "BMIcalculator" 

urlpatterns = [
    path("entry/", bmi_data_entry, name="data_entry" ),
    path("calculate-bmi/", bmi_calculator, name="bmi_calculator"),
]
 