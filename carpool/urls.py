from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from . import views

urlpatterns=[

    url('',views.home,name = 'home'),
    url('user/profile',views.profile, name = 'Uprofile'),
    url('update/',views.profile_update, name='update'),
    url('user/destination',views.destination, name = 'destination'),
    url('user/contact',views.contact, name = 'contact'),
    url('about',views.about, name = 'about'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
