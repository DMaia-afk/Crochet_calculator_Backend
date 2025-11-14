from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note
from django.db import IntegrityError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  # Confirmação

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("As senhas não coincidem.")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Este email já está registrado.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove antes de criar
        try:
            user = User.objects.create_user(
                username=validated_data['email'],  # Use email as username
                email=validated_data['email'],
                password=validated_data['password']
            )
        except IntegrityError:
            raise serializers.ValidationError("Este email já está registrado.")
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'material_cost', 'hours', 'minutes', 'hourly_rate', 'fixed_expenses', 'profit_margin', 'total_price', 'created_at')
        read_only_fields = ('id', 'created_at')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'