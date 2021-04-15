from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


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
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('user:login'))
    context = {'form':form, 'title':'Register Form'}
    return render(request, 'register.html', context)
        
