from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

from . import utils
from .serializers import *
from .models import *
import uuid

from django.contrib.auth.hashers import (
    make_password,
    is_password_usable,
    check_password,
)


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


class UserLogin(APIView):
    def post(self, request, format=None):

        email = request.data.get('email')
        password = request.data.get('password')
        if (not email) or (not password):
            return Response('Credentials is missing',
                            status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            cred = Credential.objects.get(pk=user.id)
            encrypted_pass = cred.encrypted_pass
            # This line is equalent to cred=... and encrypted_pass=...
            # encrypted_pass = user.credential.encrypted_pass
            if check_password(password, encrypted_pass):
                return Response('Success', status.HTTP_200_OK)
            else:
                return Response('Failed', status.HTTP_403_FORBIDDEN)

        except User.DoesNotExist:
            user = None
            return Response('User not found', status.HTTP_404_NOT_FOUND)


class UserRefuel(APIView):
    def post(self, request, format=None):

        refuel_serializer = GetRefuelInformationSerializer(
                                        data=request.data)
        if not refuel_serializer.is_valid():
            return Response(refuel_serializer.errors,
                            status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(tag_id=tag_id)
        except User.DoesNotExist:
            return Response('User not found', status.HTTP_404_NOT_FOUND)

        refuel = refuel_serializer.data
        refuel['user'] = user.id
        serializer = RefuelSerializer(data=refuel)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request, user_id, format=None):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
            return Response('The user has not registered',
                            status.HTTP_404_NOT_FOUND)

        try:
            refuels = Refuel.objects.get(user=user.id)
            serializer = RefuelSerializer(data=refuels, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(e.message,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

























