from django.urls import path
from my_about import views

urlpatterns = [
    path('about/', views.about, name='about'),
    ]
