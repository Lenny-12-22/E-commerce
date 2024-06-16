from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Cart,CartItem
from django.contrib.auth.decorators import login_required



@login_required
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    print("getting")
    product = get_object_or_404(Product, id=product_id)
    

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    print("processing ..")

    if not created:
        cart_item.quantity += quantity
    cart_item.save()

    return JsonResponse({'status': 'success', 'message': 'Product added to cart'})

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'basket.html', {'cart_items': cart_items})

@login_required
def update_cart_item(request):
    cart_item_id = request.POST.get('cart_item_id')
    quantity = int(request.POST.get('quantity'))

    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        status = 'success'
    else:
        cart_item.delete()
        status = 'removed'

    return JsonResponse({'status': status, 'message': 'Cart updated'})

@login_required
def remove_from_cart(request):
    cart_item_id = request.POST.get('cart_item_id')
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    return JsonResponse({'status': 'success', 'message': 'Product removed from cart'})

    