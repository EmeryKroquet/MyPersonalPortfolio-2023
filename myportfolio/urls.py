from django.contrib import admin
from django.urls import path, include

from portfolio import views


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
