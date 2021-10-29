from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, UpdateAPIView,
    ListAPIView
)
from .models import Notes
from .serializers import (
    NotesSerializer,NotesStoreSerializer,NotesUpdateSerializer
)
from commons.Authentication import Authentication
from commons.IsOwner import IsOwner
from commons.pagination import Pagination

# Create your views here.
class NotesView(ListCreateAPIView):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    authentication_classes = [ Authentication ]
    permission_classes = [ IsAuthenticated ]
    pagination_class = Pagination

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "items":[serializer.data]
        })

    def list(self, request, *args, **kwargs):
        filter = request.query_params.get("text")

        notes = self.get_queryset().filter(
            owner=request.user, 
            isStore=False,
            text__icontains=filter
        ).order_by('id')
        
        page = self.paginate_queryset(notes)
        serializer = self.get_serializer(page, many=True)
        
        return self.get_paginated_response(serializer.data)
        
        


class NotesDetail(RetrieveAPIView):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    authentication_classes = [Authentication]
    permission_classes=[IsAuthenticated, IsOwner]

    def retrieve(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = self.get_serializer(note)
        return Response({
            "items":[serializer.data]
        })

class NotesStore(UpdateAPIView):
    serializer_class = NotesStoreSerializer        
    queryset = Notes.objects.all()
    authentication_classes=[Authentication]
    permission_classes=[IsAuthenticated, IsOwner]

    def partial_update(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = self.get_serializer(note,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "items":[serializer.data]
        })

class NotesUpdate(UpdateAPIView):
    serializer_class=NotesUpdateSerializer
    queryset = Notes.objects.all()
    authentication_classes=[Authentication]
    permission_classes=[IsAuthenticated, IsOwner]

    def partial_update(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = self.get_serializer(note, data= request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "items":[serializer.data]
        })        