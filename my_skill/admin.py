from django.contrib import admin

from my_skill.models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    # Configuration for Skill model in admin
    list_display = ('name', 'description')
