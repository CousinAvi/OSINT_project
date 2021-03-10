from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Name = models.CharField(max_length=20)
    Message = models.TextField()
