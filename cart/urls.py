from django.urls import path
from . import views

urlpatterns = [
    # Add your cart view here
    path('cart/', views.cart, name='cart'),
    path('buy/', views.buy_cart, name='buy_cart')
]
