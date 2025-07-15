from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def product_list(request):
    # Placeholder for product catalogue
    return render(request, 'products/product_list.html')

def product_detail(request, pk):
    # Placeholder for product detail
    return render(request, 'products/product_detail.html')

def category_browse(request, slug):
    # Placeholder for category browsing
    return render(request, 'products/category_browse.html')

def search(request):
    # Placeholder for search
    return render(request, 'products/search.html')

def filter_products(request):
    # Placeholder for AJAX filtering
    return JsonResponse({'status': 'ok'})
