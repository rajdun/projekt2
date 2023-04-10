from django.contrib import admin
from .models import Address, UserAddressHistory, Profile


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'city', 'zip_code', 'country')
    search_fields = ('address_line_1', 'city', 'zip_code', 'country')


class UserAddressHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'date_added')
    search_fields = ('user__username', 'address__address_line_1')
    ordering = ('-date_added',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'default_address')
    search_fields = ('user__username', 'phone_number')
    ordering = ('user__username',)


admin.site.register(Address, AddressAdmin)
admin.site.register(UserAddressHistory, UserAddressHistoryAdmin)
admin.site.register(Profile, ProfileAdmin)
