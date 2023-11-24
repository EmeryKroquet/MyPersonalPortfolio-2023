from django.shortcuts import render
from .models import UserProfile


def user_profile(request, user_id):
    profile = UserProfile.objects.get(id=user_id)
    return render(request, 'profile.html', {'profile': profile})
