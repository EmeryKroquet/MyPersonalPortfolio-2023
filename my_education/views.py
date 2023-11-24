from django.shortcuts import render
from . models import Education


def education_list(request):
    educations = Education.objects.all()
    return render(request, 'my_education/education.html', {'educations': educations})
