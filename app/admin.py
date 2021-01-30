from django.contrib import admin
from .models import *
from carpool.models import *

# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Passenger)
