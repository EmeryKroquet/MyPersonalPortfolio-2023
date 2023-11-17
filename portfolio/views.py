from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, ProfessionalExperience, Certification
from .models import Home
from .models import About


def home(request):
    home_data = Home.objects.first()
    return render(request, 'home.html', {'home_data': home_data})


def about(request):
    about_data = About.objects.first()
    return render(request, 'about.html', {'about_data': about_data})


def show_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def show_skills(request):
    skills = Skill.objects.all()
    return render(request, template_name='skills.html', context={'skills': skills})


def show_experience(request):
    experiences = ProfessionalExperience.objects.all()
    return render(request, template_name='experience.html', context={'experiences': experiences})


def show_certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})


def experience_detail(request, experience_id):
    experience = get_object_or_404(ProfessionalExperience, id=experience_id)
    return render(request, 'experience_detail.html', {'experience': experience})


def certification_detail(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    return render(request, 'certification_detail.html', {'certification': certification})


def contact(request):
    return render(request, 'contact.html')
