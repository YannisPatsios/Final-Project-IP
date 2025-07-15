from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.product_crud, name='product_crud'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('users/', views.user_crud, name='user_crud'),
    path('categories/', views.category_crud, name='category_crud'),
    path('orders/', views.orders_crud, name='orders_crud'),
    path('role/', views.role_display, name='role_display'),
] 