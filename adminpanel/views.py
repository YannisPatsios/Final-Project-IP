from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from products.models import Product, Category
from django.contrib.auth.models import User
from .forms import ProductForm, CategoryForm
from cart.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.utils import timezone

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
    categories = Category.objects.all()
    return render(request, 'adminpanel/product_crud.html', {'products': products, 'form': form, 'categories': categories})

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
def user_add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = bool(request.POST.get('is_staff'))
        is_superuser = bool(request.POST.get('is_superuser'))
        if not username or not email or not password:
            return JsonResponse({'status': 'error', 'errors': 'All fields are required.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'errors': 'Username already exists.'}, status=400)
        user = User.objects.create(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            password=make_password(password)
        )
        return JsonResponse({'status': 'ok', 'id': user.id, 'username': user.username})
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = bool(request.POST.get('is_staff'))
        is_superuser = bool(request.POST.get('is_superuser'))
        if not username or not email:
            return JsonResponse({'status': 'error', 'errors': 'Username and email are required.'}, status=400)
        if User.objects.exclude(pk=pk).filter(username=username).exists():
            return JsonResponse({'status': 'error', 'errors': 'Username already exists.'}, status=400)
        user.username = username
        user.email = email
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        if password:
            user.set_password(password)
        user.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def category_crud(request):
    categories = Category.objects.all()
    return render(request, 'adminpanel/category_crud.html', {'categories': categories})

@user_passes_test(is_admin_or_editor)
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({'status': 'ok', 'id': category.id, 'name': category.name})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def orders_crud(request):
    orders = Order.objects.select_related('user').prefetch_related('items__product').order_by('-created_at')
    status_filter = request.GET.get('status', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    if status_filter:
        orders = orders.filter(status=status_filter)
    if date_from:
        orders = orders.filter(created_at__date__gte=date_from)
    if date_to:
        orders = orders.filter(created_at__date__lte=date_to)
    order_count_all = Order.objects.count()
    order_count_ongoing = Order.objects.filter(status='ongoing').count()
    order_count_completed = Order.objects.filter(status='completed').count()
    return render(request, 'adminpanel/orders_crud.html', {
        'orders': orders,
        'status_filter': status_filter,
        'date_from': date_from,
        'date_to': date_to,
        'order_count_all': order_count_all,
        'order_count_ongoing': order_count_ongoing,
        'order_count_completed': order_count_completed,
    })

@user_passes_test(is_admin_or_editor)
def order_update_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Order.STATUS_CHOICES):
            order.status = status
            order.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'errors': 'Invalid status.'}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

@user_passes_test(is_admin_or_editor)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

def role_display(request):
    role = 'Admin' if request.user.is_superuser else 'Editor'
    return render(request, 'adminpanel/role_display.html', {'role': role})
