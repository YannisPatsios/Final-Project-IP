from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_review, name='submit_review'),
    path('rate/', views.ajax_star_rating, name='ajax_star_rating'),
] 