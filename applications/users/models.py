from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UsersManager
from django.contrib.auth.models import (
    PermissionsMixin
)
from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel
)

# Create your models here.
class Users(TimeStampedModel, SoftDeletableModel, PermissionsMixin, AbstractBaseUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER = [
        (MALE,'Hombre'),
        (FEMALE,'Mujer'),
        (OTHERS,'Otro')
    ]

    email = models.EmailField(unique=True, null=False)

    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)

    nickname = models.CharField(max_length=150, null=False, default=None)

    gender = models.CharField(max_length=2, choices=GENDER, default=MALE)

    date_of_birth = models.DateField(null=True, default=None)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['name','lastname']

    objects = UsersManager()

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"    
