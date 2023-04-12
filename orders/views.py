from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderStatus


@login_required
def orders_list(request):
    status_filter = request.GET.get('status', None)

    if status_filter:
        orders = Order.objects.filter(user=request.user, status__name=status_filter).select_related(
            'status').prefetch_related('order_items__product')
    else:
        orders = Order.objects.filter(user=request.user).select_related('status').prefetch_related(
            'order_items__product')

    statuses = OrderStatus.objects.all()

    context = {'orders': orders, 'statuses': statuses, 'selected_status': status_filter}
    return render(request, 'orders/orders_list.html', context)
