from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product

# Create your views here.

@login_required
def submit_review(request):
    if request.method == 'POST' and request.is_ajax():
        form = ReviewForm(request.POST)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return JsonResponse({
                'status': 'ok',
                'rating': review.rating,
                'comment': review.comment,
                'user': review.user.username,
                'created_at': review.created_at.strftime('%Y-%m-%d %H:%M'),
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

def ajax_star_rating(request):
    return JsonResponse({'status': 'rated'})
