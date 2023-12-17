from rest_framework import serializers
from apps.authentication.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def save(self, **kwargs):
        return super().save(
            **kwargs, password=make_password(self.validated_data["password"])
        )
