from django.urls import path
from . import views

urlpatterns = [
    # URLs for Products
    path('products', views.product_list, name='product_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('products/edit/<int:pk>', views.product_update, name='product_update'),
]
