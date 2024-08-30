from rest_framework import  serializers
from .models import BlogPost, BlogLikedByUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "email"]

class BlogLikesByUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogLikedByUser
        fields = ['id', 'user', 'blog_post']

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'published_date']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = UserSerializer(instance.likes.all(), many=True).data
        return representation


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user