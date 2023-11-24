from django.contrib.auth.models import User
from django.db import models


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_achieved = models.DateField()

    def __str__(self):
        return self.name
