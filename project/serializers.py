from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'text')
        model = models.Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserBio
        fields = ('user', 'bio',)

