from django.urls import path
from . import views
# url hijo
urlpatterns = [
    path('clients', views.client_list, name='client_list'),
    path('clients/<int:pk>', views.client_detail, name='client_detail'),
    path('clients/new', views.client_create, name='client_create'),
    path('clients/edit', views.client_update, name='client_update'),
    path('clients/edit/<int:pk>', views.client_updated, name='client_updated'),
    path('clients/delete', views.client_delete, name='client_delete'),
    path('clients/delete/<int:pk>', views.client_deleted, name='client_deleted'),

]