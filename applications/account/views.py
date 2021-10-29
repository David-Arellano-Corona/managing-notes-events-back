from django.http.response import Http404
from django.shortcuts import render
from smtplib import SMTPException
from applications.users.models import Users
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    DestroyAPIView
)

from applications.users.serializers import UsersSerializers
from commons.Authentication import Authentication
from commons.exceptions import (
    UserNotFoundException
)
from commons.email import (
    email
)
# Create your views here.
class DestroyAccount(DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    authentication_classes = [ Authentication ]
    permission_classes = [ IsAuthenticated ]

    def destroy(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            self.perform_destroy(user)
            email(
                subject="Prueba",
                message="Tu cuenta ha sido dada de baja, espero vuelvas pronto",
                to = user.email,
                html_message= """
                                <p>Tu cuenta ha sido dada de baja, espero vuelvas pronto</p>
                              """
            )
        except Http404:
            raise UserNotFoundException()
        except SMTPException:
            print(f"El correo electrónico no pudo ser enviado: {user.email}")


        """
        Notificación de baja mediante email
        """
        return Response({
            "message":"success"
        })