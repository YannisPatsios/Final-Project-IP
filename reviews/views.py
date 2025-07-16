from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.db import models

# Create your views here.

@login_required
def submit_review(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if request.method == 'POST' and is_ajax:
        print('POST DATA:', request.POST)
        form = ReviewForm(request.POST)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        if form.is_valid():
            # Check for existing review
            review = Review.objects.filter(product=product, user=request.user).first()
            if review:
                review.rating = form.cleaned_data['rating']
                review.comment = form.cleaned_data['comment']
                review.save()
                created = False
            else:
                review = Review.objects.create(
                    product=product,
                    user=request.user,
                    rating=form.cleaned_data['rating'],
                    comment=form.cleaned_data['comment']
                )
                created = True
            # Calculate new average rating
            avg_rating = Review.objects.filter(product=product).aggregate(models.Avg('rating'))['rating__avg'] or 0
            return JsonResponse({
                'status': 'ok',
                'rating': review.rating,
                'comment': review.comment,
                'user': review.user.username,
                'created_at': review.created_at.strftime('%Y-%m-%d %H:%M'),
                'updated': not created,
                'avg_rating': avg_rating,
            })
        else:
            print('FORM ERRORS:', form.errors)
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        print('Invalid request: not POST or not AJAX, or user not authenticated/purchased')
        return JsonResponse({'status': 'error', 'errors': 'Invalid request.'}, status=400)

def ajax_star_rating(request):
    return JsonResponse({'status': 'rated'})
