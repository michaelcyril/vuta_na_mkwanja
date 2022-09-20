from django.urls import path
from .views import *
app_name = 'OrderingManager'

urlpatterns = [
    path('order/', CreateOrder),
    path('favourite/', CreateFavourite),
    path('myOrders/', MyOrder),
]