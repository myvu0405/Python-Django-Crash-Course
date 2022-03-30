from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message=models.CharField(max_length= 200)
    createdAt=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message

    class Meta:
        ordering=['createdAt']

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    detail=models.CharField(max_length= 200)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

    class Meta:
        ordering=['createdAt']
