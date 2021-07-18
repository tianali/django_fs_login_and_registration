from django.urls import path
from .views import *

urlpatterns = [
    path('', login_reg),
    path('user/register', create_user),
    path('user/login', login_user),
    path('user/logout', logout),
    path('dashboard', dashboard),
]