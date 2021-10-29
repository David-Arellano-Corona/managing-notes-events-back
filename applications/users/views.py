from django.shortcuts import render
from rest_framework.response import Response
from .models import Users
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import(
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
)

from .serializers import (
    UsersSerializers, SignupSerializer
)
from commons.Authentication import Authentication
# Create your views here.

class UsersView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    authentication_classes = [Authentication]   
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.get_serializer(data = request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response({
            "items":[user.data]
        })
        
    def list(self, request, *args, **kwargs):
        users = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(users, many=True)
        return Response({
            "items":serializer.data
        })    


class SignupView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = SignupSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]


    def partial_update(self, request, *args, **kwargs):
        user = self.get_serializer(self.get_object(), data = request.data, partial=True)
        user.is_valid(raise_exception = True)
        user.save()
        return Response({
            "items":[user.data]
        })        

    def retrieve(self, request, *args, **kwargs):
        users = self.get_serializer(self.get_object())
        return Response({
            "items":[users.data]
        })

    def update(self, request, *args, **kwargs):
        user = self.get_serializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()    
        return Response({
            "items":[user.data]
        })
