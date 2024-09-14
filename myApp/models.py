from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):

    USER = [
        ('admin', 'Admin'),
        ('viewer', 'Viewer')
    ]

    user_type = models.CharField(choices=USER, max_length=50, null=True)


class Resume_Model(models.Model):

    GENDER = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]    
