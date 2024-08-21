from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import  BlogPost, Publisher, BlogLikedByUser
from django.contrib.auth.models import User
from .serializers import  BlogPostSerializers, PublisherSerializers, BlogLikesByUserSerializers, RegisterSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = 'pk'

class PublisherListCreate(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers

class BlogLikedByUserListCreate(generics.ListCreateAPIView):
    serializer_class = BlogLikesByUserSerializers

    def get_queryset(self):
        blog_post_id = self.kwargs['pk']
        return BlogLikedByUser.objects.filter(blog_post_id=blog_post_id)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer