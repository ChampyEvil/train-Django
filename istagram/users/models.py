from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profiles")