from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileEditForm, AddressEditForm
from .models import Profile, UserAddressHistory, Address


@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user.id)
    except Profile.DoesNotExist:
        return redirect('home')
    address = profile.default_address
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        address_form = AddressEditForm(request.POST)

        if profile_form.is_valid() and address_form.is_valid():
            profile_form.save()
            address_form.save()

            profile.default_address = address_form.instance
            profile.save()

            history = UserAddressHistory(user=request.user, address=address_form.instance)
            history.save()

            return redirect('edit_profile')  # Załóżmy, że istnieje widok o nazwie 'profile'
    else:
        profile_form = ProfileEditForm(instance=profile)
        address_form = AddressEditForm(instance=address)

    return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form, 'address_form': address_form})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Błędny login lub hasło!'})
    return render(request, 'accounts/login.html')


@sensitive_post_parameters()
@csrf_protect
@never_cache
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            address = Address()
            address.save()

            history = UserAddressHistory(user=form.instance, address=address)
            history.save()

            profile = Profile(user=form.instance, phone_number='', default_address=address)
            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
