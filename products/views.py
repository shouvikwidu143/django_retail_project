from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import DetailView
import logging

logger = logging.getLogger("retailpro")

# Create your views here.
def test_view(request):
    return render(request, 'products/products.html')

def product_view(request):
    products = Products.objects.all()
    logger.debug("All Products: %s", str(products))
    context = {'products':products}
    return render(request, 'products/products.html', context)

class ProductDetailView(DetailView):
    model = Products
    
    def get_object(self):
        product = get_object_or_404(Products, product_slug=self.kwargs.get('product_slug'))
        # return Products.objects.filter(id=product.id).first()
        logger.debug("Selected Product: %s", str(product))
        return product