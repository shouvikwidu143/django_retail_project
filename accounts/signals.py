from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, WishList
from django.template.defaultfilters import slugify


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        WishList.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    instance.wishlist_by_user.save()
    
# @receiver(pre_save, sender=WishList)
def pre_save_wishlist_slug(sender, instance, *args, **kwargs):
    if instance.wishlist_name == "slug":
        instance.wishlist_name = slugify(instance.user.username)+"-wishlist"
        
pre_save.connect(pre_save_wishlist_slug, sender=WishList)