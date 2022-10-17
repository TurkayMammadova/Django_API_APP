from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to = 'user_avatars',blank=True, null=True)



# class Registration(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email= models.EmailField(max_length=100)
#     password = models.CharField(max_length=50)
#     confirmation_password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name