from django.shortcuts import render

def index(request):
    return render(request, 'travel/index.html')

def destinations(request):
    return render(request, 'travel/destinations.html')
