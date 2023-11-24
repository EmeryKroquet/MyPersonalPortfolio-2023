from django.contrib import admin
from my_about.models import About
from my_profiles.admin import UserProfileAdmin  # Assurez-vous d'importer UserProfileAdmin correctement


class AboutAdmin(admin.ModelAdmin):
    # Vos configurations pour AboutAdmin ici
    inlines = [UserProfileAdmin]


# Enregistrez la classe AboutAdmin avec le modèle approprié dans votre admin.py principal
admin.site.register(About, AboutAdmin)
