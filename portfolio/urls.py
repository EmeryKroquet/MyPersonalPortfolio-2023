from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('projets/', views.afficher_projets, name='projets'),
    path('competences/', views.afficher_competences, name='competences'),
    path('experience/', views.afficher_experience, name='experience'),
    path('certifications/', views.afficher_certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
]
