# from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/delete/<int:pk>/', views.OrderDeleteList.as_view(), name='order-delete'),
    path('orders/update/<int:pk>/', views.OrderRetriveUpdateList.as_view(), name='order-update')
]