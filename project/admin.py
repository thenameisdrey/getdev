from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm, UserBioForm
from . models import Post, UserBio

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = UserBio
    model = UserBioForm
    list_display = ['email', 'username', 'name']

admin.site.register(Post)
admin.site.register(UserBio)