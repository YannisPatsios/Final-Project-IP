from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.db import IntegrityError

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
            try:
                review, created = Review.objects.get_or_create(
                    product=product,
                    user=request.user,
                    defaults={
                        'rating': form.cleaned_data['rating'],
                        'comment': form.cleaned_data['comment'],
                    }
                )
                if not created:
                    review.rating = form.cleaned_data['rating']
                    review.comment = form.cleaned_data['comment']
                    review.save()
                return JsonResponse({
                    'status': 'ok',
                    'rating': review.rating,
                    'comment': review.comment,
                    'user': review.user.username,
                    'created_at': review.created_at.strftime('%Y-%m-%d %H:%M'),
                    'updated': not created,
                })
            except IntegrityError:
                return JsonResponse({'status': 'error', 'errors': 'You have already submitted a review for this product.'}, status=400)
        else:
            print('FORM ERRORS:', form.errors)
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

def ajax_star_rating(request):
    return JsonResponse({'status': 'rated'})
