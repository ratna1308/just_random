from django.shortcuts import render

from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    TODO
    References
    1. https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

    """

    serializer_class = AuthTokenSerializer
