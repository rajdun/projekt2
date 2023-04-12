from django.urls import path
from .views import add_product, products_list

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', products_list, name='products_list')
]
