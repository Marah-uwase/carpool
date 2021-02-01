from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from . import views
from .views import SignUpView


urlpatterns=[

    url(r'^$',views.home,name = 'home'),
    url('signup/', SignUpView.as_view(), name='signup'),
    url(r'^user/profile',views.profile, name = 'Uprofile'),
    url(r'^update/',views.profile_update, name='update'),
    url(r'^user/destination',views.destination, name = 'destination'),
    url(r'^user/contact',views.contact, name = 'contact'),
    url(r'^about',views.about, name = 'about'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
