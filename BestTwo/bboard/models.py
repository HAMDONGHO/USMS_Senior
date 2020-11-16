from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
