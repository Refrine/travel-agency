from django.shortcuts import render, get_object_or_404
from .models import Category, Tour

def tour(request):
    categories = Category.objects.all()
    tours = Tour.objects.all()
    return render(request, 'tours/destinations.html', {
        'categories': categories,
        'tours': tours
    })
    

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tours/tour_detail.html',{
        'tour':tour
    })



