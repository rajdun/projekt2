from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username',)
    inlines = [CartItemInline]
    ordering = ('-created_at',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity')
    list_filter = ('product__category', 'cart__created_at')
    search_fields = ('product__name', 'cart__user__username')
    ordering = ('-cart__created_at',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
