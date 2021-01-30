from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView



urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    url(r'^new_trip/$', views.new_trip, name='new_trip'),
    url(r'^home/$', views.home, name='homePage'),
    url('signup/', SignUpView.as_view(), name='signup'),
    url(r'^login/', views.signin, name='signIn'),
    url(r'^save_journey/$', views.save_journey, name='save_journey'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^search_trip/$', views.search_trip, name='search_trip'),
    url(r'^get_results/$', views.get_results, name='get_results'),
    
    url(r'^search_results/$', views.search_results, name='search_results'),
    url(r'^request_success/$', views.request_success, name='request_success'),
    url(r'^send_request/$', views.send_request, name='send_request'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    