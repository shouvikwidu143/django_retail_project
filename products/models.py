from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=255)
    parent_sku_number = models.CharField(default='', max_length=64, null=True, blank=True)
    product_sku_number = models.CharField(max_length=64, unique=True)
    product_category = models.CharField(max_length=255)
    product_brand = models.CharField(null=False, blank=False, max_length=255)
    product_manufracturer = models.CharField(null=False, blank=False, max_length=255)
    unit_price = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    min_units = models.IntegerField(default=1)
    package_units = models.IntegerField(default=1)
    date_first_available = models.DateField()
    asin_number = models.CharField(null=False, blank=False, max_length=255)
    item_model_number = models.CharField(null=False, blank=False, max_length=255)
    size_variants = models.CharField(default='', null=True, blank=True, max_length=32)
    country_of_origin = models.CharField(null=False, blank=False, max_length=64)
    packer = models.CharField(null=False, blank=False, max_length=255)
    importer = models.CharField(null=False, blank=False, max_length=255)
    included_components = models.CharField(null=False, blank=False, max_length=512)
    product_height = models.CharField(null=True, blank=True, max_length=20)
    product_width = models.CharField(null=True, blank=True, max_length=20)
    product_length = models.CharField(null=True, blank=True, max_length=20)
    product_weight = models.CharField(null=True, blank=True, max_length=20)
    product_height_dim = models.CharField(null=True, blank=True, max_length=20)
    product_width_dim = models.CharField(null=True, blank=True, max_length=20)
    product_length_dim = models.CharField(null=True, blank=True, max_length=20)
    product_weight_dim = models.CharField(null=True, blank=True, max_length=20)
    product_description = models.CharField(null=True, blank=True, max_length=512)
    product_active = models.BooleanField(default=True)
    product_expired = models.DateField(null=True, default=None, blank=True)
    product_expired_by = models.CharField(null=True, default=None, blank=True, max_length=128)
    legal_disclaimer = models.CharField(null=True, default=None, blank=True, max_length=512)
    color_available = models.CharField(null=False, max_length=128)
    featured_content = models.BooleanField(default=False, )
    size_variants = models.CharField(default='', null=True, blank=True, max_length=32)
    misc_attr_1 = models.CharField(null=True, default=None, blank=True, max_length=128)
    product_slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self):
        return self.product_name + "-" + self.product_category
    
    def get_absolute_url(self):
        return reverse('products')
    
    
class ProductSpecification(models.Model):
    product_sku_number = models.ForeignKey('Products', on_delete=models.CASCADE, to_field='product_sku_number')
    product_specs_title = models.CharField(default='x', max_length=64)
    product_specs = models.CharField(max_length=255)
    created_on = models.DateField()
    created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.DO_NOTHING)
    updated_on = models.DateField()
    uploaded_by = models.ForeignKey(User, related_name='uploaded_by_user', on_delete=models.DO_NOTHING)
    misc_attr_1 = models.CharField(null=True, default=None, blank=True, max_length=128)
    
    def __str__(self):
        return str(self.id) + ". " + self.product_sku_number.product_name

class ProductImages(models.Model):
    product_sku_number = models.ForeignKey('Products', on_delete=models.CASCADE, to_field='product_sku_number')
    product_img_url = models.CharField(max_length=255)
    active = models.BooleanField(default= True)
    date_uploaded = models.DateField()
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    misc_attr_1 = models.CharField(null=True, default=None, blank=True, max_length=128)
    
    def __str__(self):
        return str(self.id) + ". " + self.product_sku_number.product_name