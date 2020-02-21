from django.contrib import admin
from rest_framework import serializers

from extend_user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# admin.site.register(UserSerializer)