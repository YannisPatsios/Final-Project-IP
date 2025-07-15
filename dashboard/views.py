from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from reviews.models import Review
from cart.models import CartItem

# Create your views here.

@login_required
def dashboard_home(request):
    # Recently viewed: store product IDs in session
    recently_viewed_ids = request.session.get('recently_viewed', [])
    recently_viewed = Product.objects.filter(id__in=recently_viewed_ids)[:5]
    # Reviews written
    user_reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    # Cart summary
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'dashboard/home.html', {
        'recently_viewed': recently_viewed,
        'user_reviews': user_reviews,
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

def recently_viewed(request):
    return render(request, 'dashboard/recently_viewed.html')

def reviews_written(request):
    return render(request, 'dashboard/reviews_written.html')

def cart_summary(request):
    return render(request, 'dashboard/cart_summary.html')
