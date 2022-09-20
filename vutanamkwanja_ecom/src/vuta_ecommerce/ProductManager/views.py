from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *
from SystemAuth.models import User


# Views for the api

@api_view(['GET'])
@permission_classes([AllowAny])
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


# Views for the admin dashboard


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProduct(request):
    user = request.user
    us = User.objects.get(username=user)
    print(us.is_superuser)
    if not us.is_superuser:
        data = request.data
        name = data['name']
        description = data['description']
        price = data['price']
        quantity = data['quantity']
        category_id = data['category_id']
        category = Category.objects.get(id=category_id)
        images = data['images']
        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity,
                                         category_id=category)
        product.save()
        mydata = Product.objects.values('id').all()
        print(mydata)
        mySavedData = [entry for entry in mydata]
        # Need to consider the last saved product by using the maximum id of product
        if len(mySavedData) > 1:
            p_id = []
            for i in range(0, len(mySavedData) - 1):
                id = mySavedData[i]['id']
                p_id.append(id)
            last_p_id = max(p_id)
            print(last_p_id)
        elif len(mySavedData) == 1:
            last_p_id = mySavedData[0]['id']
        else:
            return Response({'message': 'Insert the product'})

        # data_id = mySavedData['id']
        myProduct = Product.objects.get(id=last_p_id)
        for img in images:
            image = img['image']
            ImageToSave = Image.objects.create(image=image, product_id=myProduct)
            ImageToSave.save()
        return Response({'message': 'successful save product'})
    return Response({'message': 'The user is not admin'})

# {
#     "name": "airnike111",
#     "description": "The new brand device",
#     "price": 30000,
#     "quantity": 30,
#     "category_id": 1,
#     "images": [{"image": "image.png"}, {"image": "image2.png"}]
# }
