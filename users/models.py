from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _


class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")


class RoleChoices(models.TextChoices):
    USER = ("user", "User")
    ADMIN = ("admin", "Admin")


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=150,
        blank=True,
        null=True,  # nullable
    )
    role = models.CharField(
        max_length=5,
        choices=RoleChoices.choices,
    )
    gender = models.CharField(
        max_length=6,
        choices=GenderChoices.choices,
    )


class UserLoginLog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    ip = models.CharField(
        max_length=39,  # IPv6
    )
