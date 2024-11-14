from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car, Metrics


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # To save password properly (hashed) when creating a new user
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['patente', 'owner']

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ['user', 'car', 'speed', 'fuel_level', 'timestamp']
