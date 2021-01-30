from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from carpool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('carpool.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')), 
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html')),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/')),
]
