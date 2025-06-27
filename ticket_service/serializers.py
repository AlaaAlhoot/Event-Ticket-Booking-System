from rest_framework import serializers
from .models import Ticket
import requests

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        event_id = validated_data['event_id']
        quantity = validated_data['quantity']


        event_url = f"http://127.0.0.1:8000/api/events/{event_id}/"
        response = requests.get(event_url)

        if response.status_code != 200:
            raise serializers.ValidationError("Event not found")

        event_data = response.json()
        available = event_data.get('available_tickets', 0)

        if quantity > available:
            raise serializers.ValidationError("Not enough tickets available")


        return super().create(validated_data)
