from django.contrib.auth import get_user_model
from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    """
        Serializer for create(register) user
    """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self):
        return get_user_model().objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
