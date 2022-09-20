from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'SystemAuth'

urlpatterns = [
    path('register/', RegisterUser),
    path('profile/', UserProfile),
    # path('', LoginUser),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
