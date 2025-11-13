from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'material_cost', 'hours', 'minutes', 'hourly_rate', 'fixed_expenses', 'profit_margin', 'total_price', 'created_at')
        read_only_fields = ('id', 'created_at')