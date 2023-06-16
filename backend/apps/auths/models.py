from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models

from abstracts.utils import generate_activate_code


class CustomUserManager(BaseUserManager):
    """
        Custom user manager
    """

    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        Custom user model
    """

    ACTIVATE_CODE_SIZE = 40

    email = models.EmailField(
        verbose_name='email',
        max_length=150,
        unique=True
    )
    surname = models.CharField(
        verbose_name='surname',
        max_length=150,
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name='name',
        max_length=150,
        null=True,
        blank=True
    )
    patronymic = models.CharField(
        verbose_name='patronymic',
        max_length=150,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='is active',
        default=False,
    )
    is_staff = models.BooleanField(
        verbose_name='is staff',
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='is superuser',
        default=False,
    )
    wallet = models.CharField(
        verbose_name='wallet',
        max_length=42,
        blank=True,
        null=True
    )
    activate_code = models.CharField(
        verbose_name='activate code',
        max_length=ACTIVATE_CODE_SIZE,
        blank=True,
        null=True
    )
    date_of_creation = models.DateTimeField(
        verbose_name='date of creation',
        auto_now_add=True
    )
    date_of_change = models.DateTimeField(
        verbose_name='date of change',
        auto_now=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs) -> None:
        self.activate_code = generate_activate_code(self.ACTIVATE_CODE_SIZE)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('email', )
