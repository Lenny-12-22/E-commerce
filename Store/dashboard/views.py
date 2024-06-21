from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem
from basket.models import Cart, CartItem
from django.http import JsonResponse



def create_order(request):
    if request.method == 'POST' and request.user.is_authenticated :
        cart = Cart.objects.get(user = request.user)
        order = Order.objects.create(user = request.user)

        for item in cart.cartitem_set.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price
            )
        cart.cartitem_set.all().delete()
        return JsonResponse({'status': 'Order created successfully', 'order_id': order.id})
    return JsonResponse({'status': 'Failed to create order'}, status=400)
