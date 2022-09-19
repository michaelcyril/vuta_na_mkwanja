from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(data=products, many=True)
    if not serializer.is_valid():
        data = serializer.data
        newdata = []
        for x in data:
            id = x['id']
            images = Image.objects.values('id', 'image', 'product_id').filter(product_id=id)
            image = [entry for entry in images]
            y = {'images': image}
            x.update(y)
            newdata.append(x)
        return Response(newdata)
    return Response({'message': 'failed to get products'})


@api_view(['GET'])
@permission_classes([AllowAny])
def Categories(request):
    data = Category.objects.all()
    serializer = CategorySerializer(data=data, many=True)
    if not serializer.is_valid():
        return Response(serializer.data)
    return Response({'message': 'failed to get categories'})

