from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class TODOUser(AbstractUser):
    email = models.EmailField(blank=True,
                              unique=True)
