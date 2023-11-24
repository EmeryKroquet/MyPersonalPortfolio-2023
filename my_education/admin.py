from django.contrib import admin

from my_education.models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'institution', 'graduation_year')
    search_fields = ('degree', 'institution')
