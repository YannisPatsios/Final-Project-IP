from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CartItem, Order, OrderItem
from products.models import Product

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'status': 'added', 'cart_count': CartItem.objects.filter(user=request.user).count()})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item:
            cart_item.delete()
            return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item and quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({'status': 'updated'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        address = request.POST.get('address', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        # Only use the fields that exist on the model
        order = Order.objects.create(
            user=request.user,
            total=total,
            address=address,
            phone=phone,
            country=country
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return render(request, 'cart/checkout.html', {'total': total, 'success': True, 'order': order})
    return render(request, 'cart/checkout.html', {'total': total, 'success': False})
