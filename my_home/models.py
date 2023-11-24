from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.CharField(max_length=500, blank=True, default="")
    image = models.ImageField(upload_to='home_images/')  # N'oubliez pas de spécifier le répertoire de téléchargement

    # des images

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return f'{self.title} - {self.subtitle}'

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return '{0} {1}'.format(self.title, self.subtitle)
