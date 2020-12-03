from django.db import models
from uuid import uuid4

class Users(models.Model):
    id = models.UUIDField(primary_key=True, max_length=255, default=uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=30)
# Create your models here.
