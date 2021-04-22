
from django.contrib import admin
from django.urls import path, include
from useraccount.views import home

app_name = "project"

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('bmi/', include("BMIcalcapp.urls", namespace="BMIcalculator")),
    path('user/', include('useraccount.urls', namespace="user")),
    path('verification/', include('verify_email.urls')),	

]
