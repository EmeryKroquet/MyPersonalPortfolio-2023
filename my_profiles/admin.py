from django.contrib import admin
from my_profiles.models import UserProfile


class UserProfileAdmin(admin.TabularInline):
    model = UserProfile


# admin.site.register(UserProfile, UserProfileAdmin)
