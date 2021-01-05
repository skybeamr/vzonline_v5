from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = 'e-mail',
        unique=True)
    is_staff = models.BooleanField(
        verbose_name = 'права редактора',
        default=False)
    is_superuser = models.BooleanField(
        verbose_name='права суперпользователя',
        default=False)
    is_active = models.BooleanField(
        verbose_name = 'учетная запись активна',
        default=True)
    date_joined = models.DateTimeField(
        verbose_name = 'дата регистрации',
        default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
