from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# from .views import addresses_view
# Create your models here.

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    return f'profile_pics/user_{instance.user.username}.{ext}'

class Addresses(models.Model):
    contact_name = models.CharField(default="NA", max_length=255)
    contact_number = models.CharField(default="NA", max_length=15)
    address_type = models.CharField(default="NA", max_length=50)
    address_1 = models.CharField(default="NA", max_length=255)
    address_2 = models.CharField(default="", null=True, blank=True, max_length=255)
    nearby_location = models.CharField(default="NA", max_length=128)
    city_or_district = models.CharField(default="NA", max_length=128)
    state = models.CharField(default="NA", max_length=128)
    country = models.CharField(default="NA", max_length=128)
    pincode = models.CharField(default="1", max_length=10)
    delivery_instructions = models.CharField(default="", null=True, blank=True, max_length=255)
    is_primary_address = models.BooleanField(default=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contact_name + "-" + self.address_type
    
    def get_absolute_url(self):
        return reverse('addresses')
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = user_directory_path)
    phone_number = models.CharField(default="", null= True, blank=True, max_length=15)
    about_me = models.TextField(default="", null= True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        