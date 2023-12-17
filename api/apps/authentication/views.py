from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.authentication.models import User
from django.shortcuts import get_object_or_404
from apps.authentication.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUserView(views.APIView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        user_serializer = UserSerializer(data=user)
        user_serializer.is_valid(raise_exception=True)
        return Response(user_serializer.data)

    def put(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        user_serializer = UserSerializer(user, data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data)
