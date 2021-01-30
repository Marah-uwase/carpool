from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.utils import timezone
from app.models import Location
from django.db import models
import datetime as dt
import cloudinary

# Create your models here.
class Passenger(models.Model):

    name = models.OneToOneField(User, related_name='driver_profile',on_delete=models.CASCADE)
    bio =  HTMLField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    current_location = models.ForeignKey('app.Location', related_name='current_location', on_delete=models.CASCADE, null=True)
    pickup_location = models.ForeignKey('app.Location',related_name='rider_pickup', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    def __str__(self):
        return str(self.name)

    def save_passenger(self):
        self.save()

    def delete_passenger(self):
        self.delete()
    


