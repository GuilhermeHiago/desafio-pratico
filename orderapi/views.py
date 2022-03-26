from gc import get_objects
from urllib import request
from django.shortcuts import render
from numpy import delete
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

# for get method overide
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import Http404


class OrderDeleteList(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        aux = super().get(request, *args, **kwargs)

        print('\n\naux:', aux.data)

        if not aux.data['owner'] == request.user.username:
            raise Http404

        return aux

    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        to_delete = Order.objects.get(self.kwargs['pk'])

        if to_delete.owner == request.user.name or request.user.is_staff:
            return super().delete(request, *args, **kwargs)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderRetriveUpdateList(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        aux = super().get(request, *args, **kwargs)

        print('\n\naux:', aux.data)

        if not aux.data['owner'] == request.user.username:
            raise Http404

        return aux
    
    @method_decorator(login_required)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @method_decorator(login_required)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        x = Order.objects.all()
        print("\n\nid:", x[0].id)

        orders = []

        if not request.user.is_staff:
            orders = [x for x in Order.objects.all() if x.owner == request.user]

        else:
            orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        order_data = request.data

        new_order = Order.objects.create(owner=request.user, product=order_data['product'], quantity=order_data['quantity'])

        new_order.save()

        serializer = OrderSerializer(new_order)

        headers = CreateModelMixin.get_success_headers(self, serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)