from django.contrib import admin
from .models import Order, OrderItem, OrderStatus


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at', 'completed')
    list_filter = ('status', 'completed', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Order, OrderAdmin)
