from django.shortcuts import render
from .models import Product

# Create your views here.

def homePage(request):
    items = Product.objects.all()
    return render(request, 'home.html', {"items":items})

def item(request, pk):
    item= Product.objects.filter(pk=pk)
    return render(request, 'item.html', {"item":item})