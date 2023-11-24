from django.contrib import admin

from my_project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Configuration for Project model in admin
    list_display = ('title', 'description', 'url', 'date')
