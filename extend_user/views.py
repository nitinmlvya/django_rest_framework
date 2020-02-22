# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

from rest_framework import viewsets
from rest_framework.response import Response
from extend_user.models import User
from extend_user.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, **kwargs):
        print('request.data: ', request.data)
        if 'is_superuser' in request.data and request.data['is_superuser'] is True:
            user = User.objects.create_superuser(**request.data)
        else:
            user = User.objects.create_user(**request.data)
        serializer = UserSerializer(user)
        return Response(serializer.data)

