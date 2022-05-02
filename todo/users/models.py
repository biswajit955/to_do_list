from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    Gender = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=Gender, default='')
    

    def __str__(self):
        return f'{self.user.username}  profile.'