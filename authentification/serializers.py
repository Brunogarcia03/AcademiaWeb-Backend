from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']  # Cambiar 'username' por 'email'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],  # Cambiar 'username' por 'email'
            password=validated_data['password']
        )
        return user