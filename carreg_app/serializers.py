from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'tag_id', 'name', 'email',
                  'credential', 'plate', 'bank', 'tel')


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'encrypted_password', 'salt')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', 'email', 'plate', 'bank', 'tel')


class RefuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refuel
        fields = ('id', 'user', 'line', 'consumption', 'refuel_time')
