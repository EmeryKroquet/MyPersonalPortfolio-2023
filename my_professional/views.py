from django.shortcuts import render, get_object_or_404
from .models import ProfessionalExperience


def professional_experience(request):
    experiences = ProfessionalExperience.objects.all()
    return render(request, 'professional_experience/experience.html',
                  {'experiences': experiences})


def experience_detail(request, experience_id):
    experience = get_object_or_404(ProfessionalExperience, id=experience_id)
    return render(request, 'professional_experience/experience_detail.html', {'experience': experience})
