from django.urls import path
from . import views

urlpatterns=[
    path('user/login', views.login_user, name='Login'),
    path('user/register_user', views.register_user, name="register_user"),
]