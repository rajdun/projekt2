from django.urls import path
from .views import add_product, products_list, buy_now

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', products_list, name='products_list'),
    path('buy/', buy_now, name='add_to_cart_or_buy')
]
