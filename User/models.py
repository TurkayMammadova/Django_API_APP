from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to = 'user_avatars',blank=True, null=True)



