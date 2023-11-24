from django.shortcuts import render, get_object_or_404

from . import models
from .models import Certification


def certifications(request):
    certification = Certification.objects.all()
    return render(request, 'my_certification/certifications.html', {'certifications': certification})


def certification_detail(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    return render(request, 'my_certification/certification_detail.html', {'certification': certification})
