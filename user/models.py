from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='profile_images', default='', blank=True, null=True)

    def __str__(self) -> str:
        return self.username



