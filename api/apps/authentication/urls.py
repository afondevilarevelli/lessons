from django.urls import path
from apps.authentication.views import CreateUserView, RetrieveUpdateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("/sign-up", CreateUserView.as_view(), name="sign-up"),
    path("/me", RetrieveUpdateUserView.as_view(), name="me"),
    path("/token", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("/token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
]
