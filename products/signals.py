
from .models import Products
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not(instance.product_slug):
        instance.product_slug = slugify(instance.product_name)+"-"+instance.product_sku_number
        
        
pre_save.connect(pre_save_product_receiver, sender=Products)