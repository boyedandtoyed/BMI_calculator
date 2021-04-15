
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/', include("BMIcalcapp.urls", namespace="BMIcalculator")),
    path('user/', include('useraccount.urls', namespace="user"))
]
