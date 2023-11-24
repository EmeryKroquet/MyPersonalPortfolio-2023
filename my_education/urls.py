from django.urls import path
from . import views

urlpatterns = [
    path('education_list/', views.education_list, name='education_list'),
]
