from rest_framework import viewsets
from extend_user.models import User
from extend_user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
