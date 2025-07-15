from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('recently-viewed/', views.recently_viewed, name='recently_viewed'),
    path('reviews-written/', views.reviews_written, name='reviews_written'),
    path('cart-summary/', views.cart_summary, name='cart_summary'),
] 