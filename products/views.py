from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Category
from django.db.models import Q

# Create your views here.

def product_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.all().order_by('-created_at')
    if query:
        products = products.filter(name__icontains=query)
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': query,
    })

def product_detail(request, pk):
    # Placeholder for product detail
    return render(request, 'products/product_detail.html')

def category_browse(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category).order_by('-created_at')
    subcategories = category.subcategories.all()
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category,
        'subcategories': subcategories,
    })

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query).order_by('-created_at')
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': query,
    })

def filter_products(request):
    # Placeholder for AJAX filtering
    return JsonResponse({'status': 'ok'})
