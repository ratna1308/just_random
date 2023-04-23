from django.shortcuts import render

from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
