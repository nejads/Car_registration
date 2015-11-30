from carreg_app.models import User, Credential, Refuel

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'plate', 'bank', 'tel')


class GetRefuelInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuel
        fields = ('tag_id', 'line', 'consumption')


class RefuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuel
