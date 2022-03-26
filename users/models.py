from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=False, null=False, default='1999-01-01')
    
    def __str__(self) -> str:
        return super().username