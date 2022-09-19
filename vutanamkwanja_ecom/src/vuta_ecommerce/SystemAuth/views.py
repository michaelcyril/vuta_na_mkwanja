# import datetime

# import jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import *
from .models import *


@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterUser(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response({'message': 'successful saved'})
    return Response({'message': 'failed to save'})


# {
#     "first_name":"Michael",
#     "last_name":"Cyril",
#     "email":"michaelcyril71@gmail.com",
#     "password":"123",
#     "username":"mike"
# }

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     username = request.data['username']
#     password = request.data['password']
#     if username is None and password is None:
#         return Response({'message': 'Username or Password is empty'})
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'message': 'User not found'})
#     if user.is_active:
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#         # token, create = Token.objects.get_or_create(user=user)
#         return Response({'jwt': token, 'user': user.id})
#     return Response({'message': 'User is not active'})



# {
#     "password":"123",
#     "username":"mike"
# }