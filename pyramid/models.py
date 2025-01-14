from django.db import models

# Create your models here.
from django.db import models
 
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
 
    def __str__(self):
        return self.username