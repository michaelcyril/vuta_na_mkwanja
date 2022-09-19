from django.urls import path
from .views import *
app_name = 'ProductManager'

urlpatterns = [
    path('Products/', AllProducts),
    path('Categories/', Categories),
]
