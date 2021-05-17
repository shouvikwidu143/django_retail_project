from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import DetailView

# Create your views here.
def test_view(request):
    return render(request, 'products/products.html')

def product_view(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products/products.html', context)

class ProductDetailView(DetailView):
    model = Products
    
    def get_object(self):
        product = get_object_or_404(Products, product_sku_number=self.kwargs.get('product_sku_number'))
        # return Products.objects.filter(id=product.id).first()
        return product