from django.contrib import admin

from my_professional.models import ProfessionalExperience


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'company', 'start_date', 'end_date')
    search_fields = ('position', 'company')
    list_filter = ('user',)
