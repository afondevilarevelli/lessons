from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.authentication.serializers import UserSerializer


class TokenWithCustomClaimsSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        user_serializer = UserSerializer(user)
        user_serializer.data

        # Add custom claims
        for k, v in user_serializer.data.items():
            token[k] = v

        return token
