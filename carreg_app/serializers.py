from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = '__all__'


class RefuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refuel
        fields = '__all__'
