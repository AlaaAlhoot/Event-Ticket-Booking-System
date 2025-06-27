from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from .models import Event, Reservation
from .serializers import EventSerializer
from django.contrib.auth.decorators import login_required
from user_service.models import UserProfile



# API Views

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'








