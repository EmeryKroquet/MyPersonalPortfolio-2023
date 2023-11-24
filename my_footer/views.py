from django.shortcuts import render
from .models import Footer


def footer(request):
    # Vous pouvez personnaliser cette vue en fonction de vos besoins spécifiques
    footer_info = Footer.objects.first()  # Obtenez le premier objet Footer, ajustez-le en fonction de votre modèle

    context = {
        'footer_info': footer_info,
    }

    return render(request, 'footer.html', context)
