from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  AbstractUser
import uuid

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)

class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, related_name='detailed_post', on_delete=models.CASCADE)

class BlogLikedByUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    liked_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    blog_post = models.ForeignKey(BlogPost, related_name='liked_blogs', on_delete=models.CASCADE)







