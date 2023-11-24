from django.db import models

from my_about.models import About


class UserProfile(models.Model):
    user = models.CharField(max_length=255)
    description = models.TextField()
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
