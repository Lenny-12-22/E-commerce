from django.urls import path
from . import views

app_name = 'buy'



urlpatterns = [
    
    path('order/', views.create_order, name="create_order"),

]