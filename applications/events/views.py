from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from commons.Authentication import Authentication
from commons.pagination import Pagination
from commons.IsOwner import IsOwner
from .models import Events
from .serializers import EventSerializer

class EventsView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.all()
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination

    def create(self, request, *args, **kwargs):
        serialize = self.get_serializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response({
            "items":[serialize.data]
        })

    def list(self, request, *args, **kwargs):
        events = self.get_queryset().filter(owner=request.user).order_by('id')
        page = self.paginate_queryset(events)
        serialize = self.get_serializer(page, many=True) 
        return self.get_paginated_response(serialize.data)

class DetailEventsView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.all()        
    authentication_classes = [Authentication]
    permission_classes = [ IsAuthenticated, IsOwner ]

    def retrieve(self, request, *args, **kwargs):
        event = self.get_object()
        serialize = self.get_serializer(event)
        return Response({
            'items':[serialize.data]
        })

    def partial_update(self, request, *args, **kwargs):
        event = self.get_object()
        serialize = self.get_serializer(event, data=request.data, partial=True) 
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response({
            'items':[serialize.data]
        })    