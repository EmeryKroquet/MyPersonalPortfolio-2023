from django.shortcuts import render, get_object_or_404

from my_project.models import Project


def projects(request):
    projets = Project.objects.all()
    print(projets)
    return render(request, 'my_project/projects.html', {'my_project': projets})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'my_project/projects_detail.html', {'my_project': project})
