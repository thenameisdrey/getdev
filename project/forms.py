from django import forms
from django.contrib.auth.models import User
from .models import UserBio, Post

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")

class UserBioForm(forms.ModelForm):

    class Meta:
        model = UserBio
        fields = ("bio",)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text")