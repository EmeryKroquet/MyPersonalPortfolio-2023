from django.shortcuts import render, get_object_or_404
from .models import Projet, Competence, ExperienceProfessionnelle, Certification


def accueil(request):
    # Logique de la vue pour la page d'accueil
    return render(request, 'accueil.html')


def afficher_projets(request):
    projets = Projet.objects.all()
    return render(request, 'projets.html', {'projets': projets})


def afficher_competences(request):
    competences = Competence.objects.all()
    return render(request, 'competences.html', {'competences': competences})


def afficher_experience(request):
    experiences = ExperienceProfessionnelle.objects.all()
    return render(request, 'experience.html', {'experiences': experiences})


def afficher_certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})


def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'detail_projet.html', {'projet': projet})


def detail_experience(request, experience_id):
    experience = get_object_or_404(ExperienceProfessionnelle, id=experience_id)
    return render(request, 'detail_experience.html', {'experience': experience})


def detail_certification(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    return render(request, 'detail_certification.html', {'certification': certification})


def contact(request):
    return render(request, 'contact.html')
