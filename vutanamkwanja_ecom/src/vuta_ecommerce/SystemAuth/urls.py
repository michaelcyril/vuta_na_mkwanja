from django.urls import path
from .views import *
app_name = 'SystemAuth'

urlpatterns = [
    path('register/', RegisterUser),
    # path('login/', login),
]