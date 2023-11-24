from django.urls import reverse
from django.shortcuts import render

from .models import Home


def home(request):
    home_data = Home.objects.all()
    return render(request, 'home.html', {'home_data': home_data})


def home_view(request):
    context = {
        'home_url': reverse('home'),
        'about_url': reverse('about'),
        'projects_url': reverse('projects'),
        # ... ajoutez d'autres URLs au besoin
    }
    return render(request, 'home.html', context)
