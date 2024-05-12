from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """Класс сериализатора для пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Класс сериализатора для регистрации пользователя"""
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "phone", "image"]
