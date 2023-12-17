from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Menu,Orders
from .serilizers import MenuSerializer,OrdersSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def home(request):
    api_urls = {
        'menu':'menu',
        'orders':'orders',
        'make-order':'make-order',
        'payments':'payments',
        'item':'item/<uuid:id>',
    }
    return Response(api_urls)


@api_view(['GET'])
def menu(request):
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def menu_item(request,id):
    item = Menu.objects.get(id=id)
    serializer = MenuSerializer(item,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createOrder(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def show_orders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_payments(request):
    payments = Payments.objects.all()
    serializer = PaymentsSerializer(payments,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_order(request,id):
    order = Orders.objects.get(id=id)
    order.delete()
    return Response('Deleted!')

    