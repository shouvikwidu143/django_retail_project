from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('', test_view, name="accounts"),
]
