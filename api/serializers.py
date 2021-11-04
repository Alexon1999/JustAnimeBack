from rest_framework import serializers
from .models import User, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    watch_list = ContentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'nom', 'prenom', 'mail', 'mdp', 'watch_list']
        extra_kwargs = {'mdp': {'write_only': True}}


class UserConnecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mail', 'mdp']
