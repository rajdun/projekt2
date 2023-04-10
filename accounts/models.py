from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    # Fields for address model
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country}, {self.zip_code}, {self.city}"


class UserAddressHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for profile model
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    default_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_amount(self):
        return self.amount / 1000000

    def set_amount(self, value):
        self.amount = value * 1000000
