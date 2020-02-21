from django.contrib.auth.models import User
from rest_framework import viewsets
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    pass


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
