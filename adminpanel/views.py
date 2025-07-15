from django.shortcuts import render

# Create your views here.

def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

def product_crud(request):
    return render(request, 'adminpanel/product_crud.html')

def user_crud(request):
    return render(request, 'adminpanel/user_crud.html')

def category_crud(request):
    return render(request, 'adminpanel/category_crud.html')

def role_display(request):
    return render(request, 'adminpanel/role_display.html')
