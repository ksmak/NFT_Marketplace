from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            "access": data["access"],
            "refresh": data["refresh"],
            "id": self.user.id,
            "username": self.user.email,
        }


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for edit user
    """
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(
        min_length=3, max_length=100, write_only=True)
    date_of_creation = serializers.DateTimeField(read_only=True)
    date_of_change = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.surname = validated_data['surname']
        instance.name = validated_data['name']
        instance.patronymic = validated_data['patronymic']
        instance.wallet = validated_data['wallet']
        instance.set_password(validated_data['password'])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ['email', 'password', 'surname', 'name', 'patronymic', 'wallet',
                  'date_of_creation', 'date_of_change']


class CreateUserSerializer(serializers.Serializer):
    """
        Serializer for create(register) user
    """
    email = serializers.EmailField(
        max_length=200, min_length=5, allow_blank=False)
    password = serializers.CharField(max_length=100)

    def create(self):
        return User.objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
