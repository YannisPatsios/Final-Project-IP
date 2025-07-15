from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Category
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Q, Avg

# Create your views here.

def product_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.all().order_by('-created_at')
    if query:
        products = products.filter(name__icontains=query)
    categories = Category.objects.filter(parent__isnull=True)

    # Recommendation logic
    recommended = []
    recently_viewed = request.session.get('recently_viewed', [])
    if recently_viewed:
        last_viewed_id = recently_viewed[0]
        try:
            last_viewed = Product.objects.get(id=last_viewed_id)
            # Recommend by category first, then brand
            recommended = Product.objects.filter(
                category=last_viewed.category
            ).exclude(id=last_viewed.id)[:4]
            if not recommended:
                recommended = Product.objects.filter(
                    brand=last_viewed.brand
                ).exclude(id=last_viewed.id)[:4]
        except Product.DoesNotExist:
            pass
    if not recommended:
        recommended = Product.objects.order_by('?')[:4]

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': query,
        'recommended': recommended,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Track recently viewed products in session
    recently_viewed = request.session.get('recently_viewed', [])
    if pk not in recently_viewed:
        recently_viewed = [pk] + recently_viewed
        recently_viewed = recently_viewed[:10]  # Keep only last 10
        request.session['recently_viewed'] = recently_viewed
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    review_form = ReviewForm()
    user_has_purchased = False
    user_review = None
    if request.user.is_authenticated:
        from cart.models import OrderItem
        user_has_purchased = OrderItem.objects.filter(
            order__user=request.user,
            order__status='completed',
            product=product
        ).exists()
        user_review = reviews.filter(user=request.user).first()
        if user_review:
            review_form = ReviewForm(instance=user_review)
        else:
            review_form = ReviewForm()
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'review_form': review_form,
        'user_has_purchased': user_has_purchased,
        'user_review': user_review,
    })

def get_descendant_category_ids(category):
    ids = [category.id]
    for subcat in category.subcategories.all():
        ids.extend(get_descendant_category_ids(subcat))
    return ids

def category_browse(request, slug):
    category = get_object_or_404(Category, slug=slug)
    # Get all descendant category IDs (including self)
    category_ids = get_descendant_category_ids(category)
    products = Product.objects.filter(category__in=category_ids).order_by('-created_at')
    subcategories = category.subcategories.all()
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category,
        'subcategories': subcategories,
    })

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query).order_by('-created_at')
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': query,
    })

def filter_products(request):
    # Placeholder for AJAX filtering
    return JsonResponse({'status': 'ok'})
