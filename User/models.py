from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name