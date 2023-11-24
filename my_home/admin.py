from django.contrib import admin
from .models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    # Ajoutez d'autres options d'administration au besoin


admin.site.register(Home, HomeAdmin)
