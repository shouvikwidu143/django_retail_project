from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import DetailView
from django.http import JsonResponse, HttpResponse
import logging

logger = logging.getLogger("retailpro")

# Create your views here.
def test_view(request):
    return render(request, 'products/products.html')

def product_view(request):
    products = Products.objects.all()
    logger.debug("Products Fetched %d", products.count())
    context = {'products':products}
    return render(request, 'products/products.html', context)

def product_json_view(request):
    if request.user.is_authenticated:
        products = list(Products.objects.values())
        return JsonResponse(products, safe=False)
    else:
        return HttpResponse("Unauthorized", status=401)

def product_detail_json_view(request, product_slug):
    products = Products.objects.values().get(product_slug=product_slug)
    return JsonResponse(products, safe=False)

class ProductDetailView(DetailView):
    model = Products
    
    def get_object(self):
        product = get_object_or_404(Products, product_slug=self.kwargs.get('product_slug'))
        # return Products.objects.filter(id=product.id).first()
        logger.debug("Selected Product: %s", str(product))
        return product