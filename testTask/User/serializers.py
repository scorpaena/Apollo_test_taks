from rest_framework import serializers
from django.contrib.auth.models import User


class AuthenticationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, 
        write_only=True, style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
