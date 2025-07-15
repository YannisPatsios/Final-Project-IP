from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def cart_view(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request):
    return JsonResponse({'status': 'added'})

def remove_from_cart(request):
    return JsonResponse({'status': 'removed'})

def update_cart(request):
    return JsonResponse({'status': 'updated'})

def checkout(request):
    return render(request, 'cart/checkout.html')
