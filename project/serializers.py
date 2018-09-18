from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('author', 'title', 'text')
        model = models.Post

