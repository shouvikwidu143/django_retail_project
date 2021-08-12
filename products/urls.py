from django.urls import path
from .views import *

urlpatterns = [
    path('', product_view, name="products"),
    path('products.json', product_json_view, name="products_json"),
    path('<slug:product_slug>/', ProductDetailView.as_view(), name="product-details"),
    path('<slug:product_slug>.json', product_detail_json_view, name="product-details-json"),
]
