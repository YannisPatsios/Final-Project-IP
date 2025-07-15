from django.shortcuts import render

# Create your views here.

def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def recently_viewed(request):
    return render(request, 'dashboard/recently_viewed.html')

def reviews_written(request):
    return render(request, 'dashboard/reviews_written.html')

def cart_summary(request):
    return render(request, 'dashboard/cart_summary.html')
