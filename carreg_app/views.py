from django.contrib.auth.hashers import (
    make_password,
    is_password_usable,
    check_password,
)

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

from . import utils
from .serializers import *
from .models import *
import uuid


def index(request):
    html = "<html><body>You do NOT need gas station any longer!</body></html>"
    return HttpResponse(html)


class UserRegisteration(APIView):
    def post(self, request, format=None):

        password = request.data.get('password')
        if not password:
            return Response('Password required', status.HTTP_400_BAD_REQUEST)

        sign_up_serializer = SignUpSerializer(data=request.data)
        if not sign_up_serializer.is_valid():
            return Response(sign_up_serializer.errors,
                            status.HTTP_400_BAD_REQUEST)

        tag_id = uuid.uuid4()

        salt = utils.salt_gen()
        encrypted_pass = make_password(password, salt=salt)
        if not is_password_usable(encrypted_pass):
            return Response('Encrypted password generation failed!',
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

        cred = Credential(salt=salt, encrypted_pass=encrypted_pass)
        cred.save()
        data = sign_up_serializer.data
        data['tag_id'] = str(tag_id)
        data['credential'] = cred.id
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
