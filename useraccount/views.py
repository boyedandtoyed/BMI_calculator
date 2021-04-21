<<<<<<< HEAD
from django.shortcuts import render, reverse
=======
from django.shortcuts import render, reverse, get_object_or_404
>>>>>>> e3fe231 (height bug correction)
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from useraccount.forms import CustomCreationForm
=======
from useraccount.forms import CustomCreationForm, CustomUpdateForm
from useraccount.models import UserModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
>>>>>>> e3fe231 (height bug correction)


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
        return HttpResponseRedirect(reverse('user:login'))
    context = {'form':form, 'title':'Register Form'}
    return render(request, 'register.html', context)
<<<<<<< HEAD
        
def logout_view(request):
   logout(request)
   return HttpResponseRedirect("/")
=======

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

def send_confirmation(request):
    pass

def send_suggestions(request):
    pass
>>>>>>> e3fe231 (height bug correction)
