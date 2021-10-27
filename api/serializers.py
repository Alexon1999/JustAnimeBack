from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'mail', 'mdp']
        extra_kwargs = {'mdp': {'write_only': True}}


class UserConnecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mail', 'mdp']
