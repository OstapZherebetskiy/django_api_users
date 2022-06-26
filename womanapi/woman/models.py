
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Woman(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name