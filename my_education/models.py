from django.contrib.auth.models import User
from django.db import models


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    graduation_year = models.PositiveIntegerField()

    def __str__(self):
        return self.degree
