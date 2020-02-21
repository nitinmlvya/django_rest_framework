from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from extend_user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # is_active = models.BooleanField(default=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        # db_table = 'auth_user'
        db_table = 'custom_user'


