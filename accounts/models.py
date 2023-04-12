from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    # Fields for address model
    address_line_1 = models.CharField(max_length=100, verbose_name='Adres:')
    address_line_2 = models.CharField(max_length=100, blank=True, verbose_name='Dodatkowy adres')
    city = models.CharField(max_length=50, verbose_name='Miasto')
    zip_code = models.CharField(max_length=10, verbose_name='Kod pocztowy')
    country = models.CharField(max_length=50, verbose_name='Kraj')

    def __str__(self):
        return f"{self.country}, {self.zip_code}, {self.city}"


class UserAddressHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for profile model
    phone_number = models.CharField(max_length=15, verbose_name='Numer telefonu')
    profile_picture = models.ImageField(upload_to='media/profile_pics', blank=True, verbose_name='Obrazek profilowy')
    default_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0, verbose_name='Kwota')

    def __str__(self):
        return self.user.username

    def get_amount(self):
        return self.amount / 1000000

    def set_amount(self, value):
        self.amount = value * 1000000
