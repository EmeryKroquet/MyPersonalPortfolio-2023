from django.contrib.auth.models import User
from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=255)
    greetings1 = models.TextField()
    greetings2 = models.TextField()
    picture = models.ImageField(upload_to='home_pictures/')
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    heading = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    description = models.TextField()
    profile_img = models.ImageField(upload_to='about_profile_images/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading


class UserProfile(models.Model):
    user = models.CharField(max_length=255)
    description = models.TextField()
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    graduation_year = models.PositiveIntegerField()

    def __str__(self):
        return self.degree


class ProfessionalExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    date_achieved = models.DateField()

    def __str__(self):
        return self.name
