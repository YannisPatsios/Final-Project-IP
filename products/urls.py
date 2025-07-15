from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_browse, name='category_browse'),
    path('search/', views.search, name='search'),
    path('filter/', views.filter_products, name='filter_products'),
] 