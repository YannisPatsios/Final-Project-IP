from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def submit_review(request):
    return render(request, 'reviews/submit_review.html')

def ajax_star_rating(request):
    return JsonResponse({'status': 'rated'})
