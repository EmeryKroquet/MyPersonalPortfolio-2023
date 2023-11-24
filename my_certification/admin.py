from django.contrib import admin
from .models import Certification


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_organization', 'date_achieved')
    search_fields = ('name', 'issuing_organization')


admin.site.register(Certification, CertificationAdmin)
