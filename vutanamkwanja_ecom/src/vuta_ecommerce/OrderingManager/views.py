from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *
from SystemAuth.models import User

from ProductManager.models import Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateOrder(request):
    mydata = request.data
    user = request.user
    us = User.objects.get(username=user)
    order = Order.objects.create(user_id=us)
    order.save()
    data = Order.objects.values('id').all()
    mySavedData = [entry for entry in data]
    # print(data)
    # try:
    #     mySavedOrder = [entry for entry in data][len(data)-1]
    #     print(mySavedOrder)
    # except IndexError:
    #     mySavedOrder = [entry for entry in data][0]
    # od_id = mySavedOrder['id']
    # Upuuzi
    if len(mySavedData) > 1:
        o_id = []
        for i in range(0, len(mySavedData) - 1):
            id = mySavedData[i]['id']
            o_id.append(id)
        od_id = max(o_id)
        print(od_id)
    elif len(mySavedData) == 1:
        od_id = mySavedData[0]['id']
    else:
        return Response({'message': 'Insert the order'})

    for dat in mydata:
        theOrder = Order.objects.get(id=od_id)
        theProduct = Product.objects.get(id=dat['product_id'])
        theQuantity = dat['quantity']
        order_product = OrderProduct.objects.create(product_id=theProduct, order_id=theOrder, quantity=theQuantity)
        if order_product:
            order_product.save()
    return Response({'message': 'successful making order'})

# [
#     {
#         "product_id": 1,
#         "quantity": 2
#     },
#     {
#         "product_id": 2,
#         "quantity": 2
#     }
# ]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateFavourite(request):
    mydata = request.data
    user = request.user
    us = User.objects.get(username=user)
    for dat in mydata:
        theProduct = Product.objects.get(id=dat['product_id'])
        MyFavourite = Favourite.objects.create(product_id=theProduct, user_id=us)
        if MyFavourite:
            MyFavourite.save()
    return Response({'message': 'successful making favourite'})

# [
#     {
#         "product_id": 1
#     },
#     {
#         "product_id": 2
#     }
# ]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyOrder(request):
    user = request.user
    us = User.objects.get(username=user)
    orders = Order.objects.values('id', 'user_id', 'is_done', 'created_at').filter(user_id=us)
    data = [entry for entry in orders]
    context = []
    for od in data:
        order_id = od['id']
        id = Order.objects.get(id=order_id)
        products = OrderProduct.objects.values('id', 'product_id', 'quantity').filter(order_id=id)
        myOrderProduct = [entry for entry in products]
        p = []
        for myop in myOrderProduct:
            id = myop['product_id']
            product = Product.objects.values('id', 'name', 'description', 'price').get(id=id)
            p.append(product)
        dOrder = {
            'order': od,
            'products': p
        }
        context.append(dOrder)
    print(context)
    return Response(context)

