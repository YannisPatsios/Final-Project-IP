from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    # Placeholder for logout
    pass

def profile_edit(request):
    return render(request, 'accounts/profile_edit.html')
