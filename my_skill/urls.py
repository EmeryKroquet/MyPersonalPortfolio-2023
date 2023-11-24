from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.show_skills, name='show_skills'),
]
