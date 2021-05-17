from django.urls import path
from .views import *

urlpatterns = [
    path('', product_view, name="products"),
    # path('<int:pk>/', ProductDetailView.as_view(), name="product-details"),
    path('<str:product_sku_number>/', ProductDetailView.as_view(), name="product-details"),
]
