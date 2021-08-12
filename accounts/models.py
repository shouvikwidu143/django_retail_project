from products.models import Products
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from products.models import Products
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
            
class WishList(models.Model):
    wishlist_name = models.SlugField(default="slug", max_length=255, null=True, blank=True, unique= True)
    user = models.OneToOneField(User, related_name='wishlist_by_user', on_delete=models.CASCADE)
    added_on = models.DateField(auto_now = True)
    misc_attr_1 = models.CharField(null=True, default=None, blank=True, max_length=128)
    
    def __str__(self):
        return f'{self.user.username}\'s wishlist'
    
    def get_absolute_url(self):
        return reverse('profile')
    
class WishListItem(models.Model):
    user_wishlist = models.ForeignKey(WishList, related_name='wishlist_owner', on_delete=models.CASCADE)
    product_sku_number = models.ForeignKey(Products, on_delete=models.CASCADE, to_field='product_sku_number')
    added_on = models.DateField(auto_now = True)
    misc_attr_1 = models.CharField(null=True, default=None, blank=True, max_length=128)
    
    def __str__(self):
        return f'{self.user_wishlist.user.username}\'s wishlist item {self.product_sku_number.product_name}'