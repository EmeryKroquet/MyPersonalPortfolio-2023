from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='my_project/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
