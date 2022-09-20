from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *
import requests

url = "http://172.17.20.159:8000/"
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

# for login********* use
# {
#     "password":"123",
#     "username":"mike"
# }


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserProfile(request):
    user = request.user
    profile = User.objects.values('id', 'first_name', 'last_name', 'email', 'username', 'phone').get(username=user)
    return Response(profile)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def LoginUser(request):
    # myurl = url+"/User/login/"
    # data = request.data
    # log = requests.post(url=myurl, json=data).status_code
    # print(log)
    # pass

