from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_profile'
