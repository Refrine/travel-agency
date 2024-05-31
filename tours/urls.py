from django.urls import path
from . import views


app_name = 'tours'

urlpatterns = [
    path('', views.tour, name='destinations'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
]
