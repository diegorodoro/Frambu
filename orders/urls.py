from django.urls import path
from . import views
from .views import OrderAPIView, OrderAPIView2

# url hijo
urlpatterns = [
    path('home', views.home, name='home'),    
    path('orders', views.order_list, name='order_list'),
    path('orders/<int:pk>', views.order_detail, name='order_detail'),
    path('orders/new', views.order_create, name='order_create'),
    path('orders/edit', views.order_update, name='order_update'),
    path('orders/edit/<int:pk>', views.order_updated, name='order_updated'),
    path('orders/delete', views.order_delete, name='order_delete'),
    path('orders/delete/<int:pk>', views.order_deleted, name='order_deleted'),
    path('ordersapi', OrderAPIView.as_view(), name='order_api'),
    path('ordersapi2', OrderAPIView2.as_view(), name='order_api2'),
]