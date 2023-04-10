from django import forms
from django.contrib.auth.models import User
from .models import Profile, Address


class AddressEditForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'zip_code', 'country']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_picture']
