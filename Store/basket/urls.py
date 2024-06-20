from django.urls import path
from . import views

app_name= 'basket'


urlpatterns=[
    path('', views.view_cart, name="view_cart"),
    path('basket_add/', views.add_to_cart, name="add_to_cart"),
    path('update_cart/', views.update_cart_item, name='update_cart_item'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
]