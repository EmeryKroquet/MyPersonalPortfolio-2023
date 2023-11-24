from django.urls import path

from . import views

urlpatterns = [
    path('certifications/', views.certifications, name='certifications'),
    path('certifications/<int:certification_id>/', views.certification_detail, name='certification_detail'),
]