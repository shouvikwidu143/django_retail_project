from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProductsResource(resources.ModelResource):
    
    class Meta:
        model = Products
        
class ProductSpecificationResource(resources.ModelResource):
    
    class Meta:
        model = ProductSpecification
        
class ProductImagesResource(resources.ModelResource):
    
    class Meta:
        model = ProductImages
        
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