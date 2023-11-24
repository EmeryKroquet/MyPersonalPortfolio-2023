from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_home.urls')),
    path('', include('my_skill.urls')),
    path('', include('my_project.urls')),
    path('my_about/', include('my_about.urls')),
    path('my_footer/', include('my_footer.urls')),
    path('my_professional/', include('my_professional.urls')),
    path('my_contact/', include('my_contact.urls')),
    path('my_profiles/', include('my_profiles.urls')),
    path('my_education/', include('my_education.urls')),
    path('certifications/', include('my_certification.urls')),
]

handler500 = 'myportfolio.views.handler500'
handler404 = 'myportfolio.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
