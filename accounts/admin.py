from django.contrib import admin
from .models import Profile, Addresses, WishList, WishListItem

# Register your models here.

admin.site.register(Profile)
admin.site.register(Addresses)
admin.site.register(WishList)
admin.site.register(WishListItem)