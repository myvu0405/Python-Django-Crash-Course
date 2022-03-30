from django.db import models

from django.contrib.auth.models import User


class Listing(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length= 200)
    description=models.CharField(max_length= 200)
    price=models.IntegerField()
    location=models.CharField(max_length= 200)
    contact=models.CharField(max_length= 200)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['createdAt']
