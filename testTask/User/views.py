from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .serializers import AuthenticationSerializer


class Login(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            data = {'error': 'Check username/password'}
            return Response(data, status=HTTP_404_NOT_FOUND)
        else:
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'token': token.key}, status=HTTP_200_OK)

def logout_view(request):
    logout(request)
    data = {'You are logged out'}
    return HttpResponse(data)
