from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


# from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('carpool.urls')),
    # url( r'^accounts/', include('django_registration.backends.one_step.urls')),
    url('accounts/', include('carpool.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
    # url(r'^logout/$',views.logout, {"next_page": '/'}),
    url('logout/', auth_views.LogoutView.as_view(), {"next_page": '/'})
    
]