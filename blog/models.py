from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATIC_CHOICES = (('draft','Draft'),('published','Publised'))
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATIC_CHOICES,default='draft')


class Meta:
    ordering = ('-publish',)
def __str__(self):
    return self.title

# Create your models here.
