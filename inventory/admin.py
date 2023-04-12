from django.contrib import admin
from .models import Category, Product, Inventory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at', 'is_active')
    list_filter = ('category', 'is_active',)
    search_fields = ('name', 'category__name',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    def get_price(self, obj):
        return obj.price / 1000000

    get_price.short_description = 'Price (in millions)'


admin.site.register(Product, ProductAdmin)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('product__name',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Inventory, InventoryAdmin)
