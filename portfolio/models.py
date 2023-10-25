from django.contrib.auth.models import User
from django.db import models


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    # Lien vers le projet en ligne, peut être optionnel
    url = models.URLField(blank=True, null=True)
    # Champ pour télécharger l'image du projet
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.titre


class Competence(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.utilisateur.username


class Education(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    diplome = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    annee_obtention = models.PositiveIntegerField()

    def __str__(self):
        return self.diplome


class ExperienceProfessionnelle(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.poste} chez {self.entreprise}"


class Certification(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    organisme = models.CharField(max_length=200)
    date_obtention = models.DateField()

    def __str__(self):
        return self.nom
