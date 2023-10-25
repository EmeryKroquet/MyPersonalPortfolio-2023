from django.contrib import admin
from .models import Projet, Competence, ProfilUtilisateur, Education, ExperienceProfessionnelle, Certification


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'url', 'date')
    # Ajoutez d'autres options d'administration si nécessaire


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    # Ajoutez d'autres options d'administration si nécessaire


@admin.register(ProfilUtilisateur)
class ProfilUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'description')
    # Ajoutez d'autres options d'administration si nécessaire


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'diplome', 'etablissement', 'annee_obtention')
    # Ajoutez d'autres options d'administration si nécessaire


@admin.register(ExperienceProfessionnelle)
class ExperienceProfessionnelleAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'poste', 'entreprise', 'date_debut', 'date_fin', 'description')
    # Ajoutez d'autres options d'administration si nécessaire


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'nom', 'organisme', 'date_obtention')
    # Ajoutez d'autres options d'administration si nécessaire
