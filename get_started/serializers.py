from rest_framework import serializers
from get_started.models import User

class UserSerializer(serializers.ModelSerializer):
    # Specify "username" field below will override the "username" of the model or you can add extra fields to a
    # ModelSerializer as per your needs.
    # username = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        # Specific fields to be returned to the response
        # fields = ['username', 'password', 'is_active']