from django.shortcuts import render
from rest_framework import generics
from . import models
from .forms import PostForm
from . import serializers

from .models import Post, UserBio
from .serializers import PostSerializer, UserSerializer

from django.contrib.auth.decorators import login_required

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = models.UserBio.objects.all()
    serializer_class = serializers.UserSerializer


@login_required
def add_post(request):    
   form = PostForm(request.POST or {})    
   if form.is_valid():
        temp = form.save(commit=False)
        temp.author = request.user # add the logged in user, as the
                                   # author
        temp.save()
 
