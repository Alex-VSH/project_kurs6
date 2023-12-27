from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=False, verbose_name='активирован')
    token = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []