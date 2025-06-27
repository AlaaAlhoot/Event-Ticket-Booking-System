from rest_framework import generics
from .models import Organizer
from .serializers import OrganizerSerializer

class OrganizerCreateView(generics.CreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class OrganizerListView(generics.ListAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
