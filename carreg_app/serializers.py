from rest_framework import serializers

from carreg_app.models import UserManager, User, Refuel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
        )
        read_only_fields = (
            User.USERNAME_FIELD,
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            User._meta.pk.name,
            'password',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class GetRefuelInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuel
        fields = ('tag_id', 'line', 'consumption')


class RefuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuel
