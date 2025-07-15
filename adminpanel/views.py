from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from products.models import Product, Category
from django.contrib.auth.models import User
from .forms import ProductForm
from cart.models import Order

def is_admin_or_editor(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin_or_editor)
def admin_dashboard(request):
    role = 'Admin' if request.user.is_superuser else 'Editor'
    return render(request, 'adminpanel/dashboard.html', {'role': role})

@user_passes_test(is_admin_or_editor)
def product_crud(request):
    products = Product.objects.all()
    form = ProductForm()
    return render(request, 'adminpanel/product_crud.html', {'products': products, 'form': form})

@user_passes_test(is_admin_or_editor)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return JsonResponse({'status': 'ok', 'id': product.id, 'name': product.name})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def user_crud(request):
    users = User.objects.all()
    return render(request, 'adminpanel/user_crud.html', {'users': users})

@user_passes_test(is_admin_or_editor)
def category_crud(request):
    categories = Category.objects.all()
    return render(request, 'adminpanel/category_crud.html', {'categories': categories})

@user_passes_test(is_admin_or_editor)
def orders_crud(request):
    orders = Order.objects.select_related('user').prefetch_related('items__product').order_by('-created_at')
    return render(request, 'adminpanel/orders_crud.html', {'orders': orders})

def role_display(request):
    role = 'Admin' if request.user.is_superuser else 'Editor'
    return render(request, 'adminpanel/role_display.html', {'role': role})
