from django.urls import path
<<<<<<< HEAD
from BMIcalcapp.views import bmi_calculator, bmi_data_entry
=======
from BMIcalcapp.views import bmi_calculator, bmi_data_entry, save_data, dashboard, delete_data
>>>>>>> e3fe231 (height bug correction)

app_name = "BMIcalculator" 

urlpatterns = [
    path("entry/", bmi_data_entry, name="data_entry" ),
    path("calculate-bmi/", bmi_calculator, name="bmi_calculator"),
<<<<<<< HEAD
=======
    path('save/', save_data, name="save"),
    path('dashboard/' ,dashboard, name="dashboard"),
    path('delete-data/', delete_data, name="delete"),
>>>>>>> e3fe231 (height bug correction)
]
 