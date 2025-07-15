from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.product_crud, name='product_crud'),
    path('users/', views.user_crud, name='user_crud'),
    path('categories/', views.category_crud, name='category_crud'),
    path('role/', views.role_display, name='role_display'),
] 