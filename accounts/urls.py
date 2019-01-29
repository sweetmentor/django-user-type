from django.urls import path, include
from accounts.views import login, register_seller, register_buyer, profile, logout


urlpatterns = [
    path('login', login, name='login'),
    path('login/seller', register_seller, name='register_seller'),
    path('login/buyer', register_buyer, name='register_buyer'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    
]