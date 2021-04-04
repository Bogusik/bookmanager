from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):

        flag = User.objects.filter(
            Q(username=data.get('username')) | Q(email=data.get('email'))
        ).exists()

        if flag:
            raise serializers.ValidationError(
                "User with current email or username exists."
            )

        return data

    def create(self, validated_data):

        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
