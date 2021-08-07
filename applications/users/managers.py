from django.db import models
from django.contrib.auth.models import (
    BaseUserManager
)

class UsersManager(BaseUserManager,models.Manager):

    def __create_user(self,email, password, is_staff, is_superadmin,**kwargs):
        user = self.model(
            email = email,
            name = kwargs.get('name',''),
            lastname = kwargs.get('lastname',''),
            nickname = kwargs.get('nickname',''),
            gender = kwargs.get('gender','M'),
            date_of_birth = kwargs.get('date_of_birth',None),
            is_staff = is_staff,
            is_superuser = is_superadmin
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password,**kwargs):
        user = self.__create_user(
            email = email,
            password = password,
            is_staff = False,
            is_superadmin = False,
            **kwargs
        )   
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.__create_user(
            email = email,
            password = password,
            is_staff = True,
            is_superadmin = True,
            **kwargs
        )     
        return user