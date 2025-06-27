from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Ticket
from .serializers import TicketSerializer
from user_service.models import UserProfile


class TicketListByUserView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        secure_token = self.kwargs['user_id']
        profile = get_object_or_404(UserProfile, secure_token=secure_token)

        if profile.user != self.request.user:
            return Ticket.objects.none()  # Prevent unauthorized access

        return Ticket.objects.filter(user=profile.user)

#  Create a new ticket
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#  Retrieve details of a specific ticket by ticket_id
class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'ticket_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)
