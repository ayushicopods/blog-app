from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import  BlogPost, BlogLikedByUser
from django.contrib.auth.models import User
from .serializers import  BlogPostSerializers, BlogLikesByUserSerializers, RegisterSerializer
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = 'pk'

class BlogLikedByUserListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogLikesByUserSerializers

    def get_queryset(self):
        blog_post_id = self.kwargs['pk']
        return BlogLikedByUser.objects.filter(blog_post_id=blog_post_id)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
