from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, Category
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import can_manage_inventory


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
