from django.shortcuts import render

from my_about.models import About


def about(request):
    about_data = About.objects.all()
    return render(request, 'about.html', {'about_data': about_data})
