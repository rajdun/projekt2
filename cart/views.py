from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cart, CartItem
from orders.models import Order, OrderItem, OrderStatus
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from inventory.models import Inventory


@login_required
def cart(request):
    # Get the current user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Calculate the total value of the cart
    cart_items = CartItem.objects.filter(cart=cart)
    total_value = sum(item.product.get_price() * item.quantity for item in cart_items)

    # Render the cart page with the cart items and total value
    context = {'cart_items': cart_items, 'total_value': total_value}
    return render(request, 'cart/cart.html', context)


@login_required
def buy_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    profile = get_object_or_404(Profile, user=request.user)
    order_status = get_object_or_404(OrderStatus, id=1)

    cart_items = CartItem.objects.filter(cart=cart)
    total_value = round(sum(item.product.get_price() * item.quantity for item in cart_items), 2)

    if total_value > profile.get_amount():
        return redirect('cart')

    order = Order()
    order.user = request.user
    order.status = order_status
    order.address = profile.default_address
    order.save()

    for item in cart_items:
        inventory = get_object_or_404(Inventory, product=item.product)
        if item.quantity > inventory.quantity:
            order.delete()
            return redirect('cart')
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item.product
        order_item.quantity = item.quantity
        inventory.quantity = inventory.quantity - item.quantity
        order_item.save()
        inventory.save()

    cart_items.delete()
    profile.set_amount(profile.get_amount() - total_value)
    profile.save()
    return redirect('orders_list')
