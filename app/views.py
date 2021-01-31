from .forms import *
from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
   '''logout view'''

def home(request):
    date = dt.date.today()

    return render(request, 'index.html',locals())


def profile_info(request):
    current_user = request.user

    return render(request, 'driver/profile.html',locals())

def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = current_user
            add.save()
        return redirect('home')

    else: 
        form = UpdateForm()
    return render(request, 'driver/update_profile.html',{'form':form})

def about(request):
    return render(request, 'app/about.html')

def destination(request):
    return render(request, 'driver/destination.html')


def contact(request):
    return render(request, 'driver/contact.html')