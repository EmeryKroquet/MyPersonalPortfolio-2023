from django.shortcuts import render

from my_skill.models import Skill


def show_skills(request):
    skills = Skill.objects.all()
    return render(request, template_name='my_skills/skills.html', context={'skills': skills})

