from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework import generics
from django.views import generic
import datetime as dt

# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
   '''logout view'''

def home(request):
    date = dt.date.today()

    return render(request, 'index.html',locals())


def profile(request):
    current_user = request.user

    return render(request, 'user/profile.html',locals())

def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = current_user
            add.save()
        return redirect('driver/home.html')

    else: 
        form = UpdateForm()
    return render(request, '/',{'form':form})


def about(request):
    return render(request, 'app/about.html')

def destination(request):
    return render(request, 'driver/destination.html')


def contact(request):
    return render(request, 'driver/contact')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'    

