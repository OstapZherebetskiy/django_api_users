from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, unique=True, null=False)
    text = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
