from django.http import HttpResponse

from rest_framework import generics, permissions, status, response, views
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
import djoser
from djoser import views, signals, settings, serializers

# from carreg import settings
from . import serializers, utils


def index(request):
    html = "<html><body>You do NOT need gas station any longer!</body></html>"
    return HttpResponse(html)


class UserRegisteration(djoser.views.RegistrationView):

    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    subject_template_name = 'activation_email_subject.txt'
    plain_body_template_name = 'activation_email_body.txt'

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        signals.user_registered.send(sender=self.__class__, user=instance,
                                     request=self.request)
        if settings.get('SEND_ACTIVATION_EMAIL'):
            self.send_email(**self.get_send_email_kwargs(instance))


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

























