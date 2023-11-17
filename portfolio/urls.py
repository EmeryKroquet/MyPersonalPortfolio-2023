from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.show_projects, name='show_projects'),
    path('skills/', views.show_skills, name='show_skills'),
    path('experience/', views.show_experience, name='show_experience'),
    path('certifications/', views.show_certifications, name='show_certifications'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('experience/<int:experience_id>/', views.experience_detail, name='experience_detail'),
    path('certifications/<int:certification_id>/', views.certification_detail, name='certification_detail'),
    path('contact/', views.contact, name='contact'),
]
