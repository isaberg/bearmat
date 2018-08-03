from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Search, Business, Favorite
admin.site.register(User, Search, Business)
