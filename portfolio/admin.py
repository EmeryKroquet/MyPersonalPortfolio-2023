from django.contrib import admin
from .models import Project, Skill, UserProfile, Education, ProfessionalExperience, Certification, About


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Configuration for Project model in admin
    list_display = ('title', 'description', 'url', 'date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    # Configuration for Skill model in admin
    list_display = ('name', 'description')


class UserProfileAdmin(admin.TabularInline):  # Use TabularInline or StackedInline based on your preference
    model = UserProfile
    extra = 1  # Number of empty forms to display for adding related objects


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Configuration for About model in admin
    inlines = [UserProfileAdmin]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    # Configuration for Education model in admin
    list_display = ('user', 'degree', 'institution', 'graduation_year')


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    # Configuration for ProfessionalExperience model in admin
    list_display = ('user', 'position', 'company', 'start_date', 'end_date', 'description')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    # Configuration for Certification model in admin
    list_display = ('user', 'name', 'issuing_organization', 'date_achieved')
