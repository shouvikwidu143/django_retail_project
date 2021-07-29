from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import *

# Register your models here.

class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductsResource
    
class ProductSpecificationAdmin(ImportExportModelAdmin):
    resource_class = ProductSpecificationResource
    
class ProductImagesAdmin(ImportExportModelAdmin):
    resource_class = ProductImagesResource
    list_display = [field.name for field in ProductImages._meta.get_fields()]
    
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductImages, ProductImagesAdmin) 
admin.site.register(ProductSpecification, ProductSpecificationAdmin)