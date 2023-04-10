from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Fields for address model
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for profile model
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    default_address = models.ForeignKey(Address, on_delete=models.CASCADE)
