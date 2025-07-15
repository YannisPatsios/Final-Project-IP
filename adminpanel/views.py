from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from products.models import Product, Category
from django.contrib.auth.models import User

def is_admin_or_editor(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin_or_editor)
def admin_dashboard(request):
    role = 'Admin' if request.user.is_superuser else 'Editor'
    return render(request, 'adminpanel/dashboard.html', {'role': role})

@user_passes_test(is_admin_or_editor)
def product_crud(request):
    products = Product.objects.all()
    return render(request, 'adminpanel/product_crud.html', {'products': products})

@user_passes_test(is_admin_or_editor)
def user_crud(request):
    users = User.objects.all()
    return render(request, 'adminpanel/user_crud.html', {'users': users})

@user_passes_test(is_admin_or_editor)
def category_crud(request):
    categories = Category.objects.all()
    return render(request, 'adminpanel/category_crud.html', {'categories': categories})

def role_display(request):
    role = 'Admin' if request.user.is_superuser else 'Editor'
    return render(request, 'adminpanel/role_display.html', {'role': role})
