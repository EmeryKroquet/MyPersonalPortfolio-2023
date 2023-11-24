from django.urls import path
from . import views

urlpatterns = [
    path('professional-experience/', views.professional_experience, name='professional_experience'),
    path('professional-experience/<int:experience_id>/', views.experience_detail, name='experience_detail'),
]
