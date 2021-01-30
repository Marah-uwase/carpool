from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Trip, Request



admin.site.register(CustomUser)
admin.site.unregister(Group)
admin.site.register(Trip)
admin.site.register(Request)