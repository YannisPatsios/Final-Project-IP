from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.product_crud, name='product_crud'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('users/', views.user_crud, name='user_crud'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/edit/<int:pk>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('categories/', views.category_crud, name='category_crud'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('orders/', views.orders_crud, name='orders_crud'),
    path('orders/update-status/<int:pk>/', views.order_update_status, name='order_update_status'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('role/', views.role_display, name='role_display'),
] 