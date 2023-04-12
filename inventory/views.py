from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category, Inventory
from accounts.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import can_manage_inventory
from orders.models import Order, OrderItem, OrderStatus


def products_list(request):
    category_filter = request.GET.get('category', None)

    if category_filter:
        products = Product.objects.select_related('inventory', 'category').filter(category__name=category_filter,
                                                                                  inventory__quantity__gt=0)
    else:
        products = Product.objects.select_related('inventory', 'category').filter(inventory__quantity__gt=0)

    categories = Category.objects.all()

    context = {'products': products, 'categories': categories, 'selected_category': category_filter}
    return render(request, 'inventory/products_list.html', context)


@login_required
def buy_now(request):
    if request.method == 'POST':
        if request.POST['action'] == 'buy_now':
            product_id = request.POST['product_id']
            quantity = int(request.POST['quantity'])

            product = get_object_or_404(Product, id=product_id)
            inventory = get_object_or_404(Inventory, product=product)
            status = get_object_or_404(OrderStatus, pk=1)
            profile = get_object_or_404(Profile, user=request.user)

            if quantity > inventory.quantity:
                return redirect('products_list')

            if product.get_price() * quantity > profile.get_amount():
                return redirect('products_list')

            order = Order()
            order.user = request.user
            order.status = status
            order.save()

            order_item = OrderItem()
            order_item.order = order
            order_item.product = product
            order_item.quantity = quantity

            inventory.quantity = inventory.quantity - quantity
            profile.amount = profile.amount - product.price * quantity
            profile.save()
            inventory.save()
            order_item.save()

            return redirect('orders_list')
        else:
            return redirect('products_list')
    else:
        return redirect('products_list')


@login_required
@user_passes_test(can_manage_inventory)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})
