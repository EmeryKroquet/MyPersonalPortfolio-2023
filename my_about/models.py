from django.db import models


class About(models.Model):
    heading = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    description = models.TextField()
    profile_img = models.ImageField(upload_to='about_profile_images/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
