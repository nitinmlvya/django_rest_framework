from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"
