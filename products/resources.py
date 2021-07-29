from import_export import resources
from .models import *

class ProductsResource(resources.ModelResource):
    
    class Meta:
        model = Products
        import_id_fields = ('product_sku_number',)
        
class ProductSpecificationResource(resources.ModelResource):
    
    class Meta:
        model = ProductSpecification
        
class ProductImagesResource(resources.ModelResource):
    
    class Meta:
        model = ProductImages