from django.urls import path
from .views import login_view, logout_view, register_view, edit_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('edit/', edit_profile, name='edit_profile')
]
