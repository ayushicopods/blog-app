from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
# if user deleted any post related to that user also gets deleted that why we are using cascade
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
#  Blog post can be liked by multiple user and the user can like
#  multiple post also that why it will be having many-to-many relation
    likes = models.ManyToManyField(User, through='BlogLikedByUser')


class BlogLikedByUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    blog_post = models.ForeignKey(BlogPost, related_name='liked_blogs', on_delete=models.CASCADE)









