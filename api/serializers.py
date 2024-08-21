from rest_framework import  serializers

from .models import BlogPost, Publisher, BlogLikedByUser
from django.contrib.auth.models import User

class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'designation']
class BlogPostSerializers(serializers.ModelSerializer):
    publisher = PublisherSerializers()
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'publisher', 'published_date']

    def create(self, validated_data):
        publisher_data = validated_data.pop('publisher')
        publisher, created = Publisher.objects.get_or_create(**publisher_data)
        blog_post = BlogPost.objects.create(publisher=publisher, **validated_data)
        return blog_post

class BlogLikesByUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogLikedByUser
        fields = ['id', 'name', 'blog_post']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2"]

    def validate(self, attrs):
       if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password , Password field didn't match"})
       return attrs

    def create(self, validated_data):
        print("validated data",validated_data)
        user = User.objects.all()
        user = User.objects.create_user(**validated_data)
        return user