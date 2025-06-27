from rest_framework import serializers
from .models import Payment
import requests

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        ticket_id = validated_data['ticket_id']
        user_id = validated_data['user_id']

        # Get ticket details
        ticket_response = requests.get(f"http://127.0.0.1:8000/api/tickets/{ticket_id}/")
        if ticket_response.status_code != 200:
            raise serializers.ValidationError("Ticket not found")
        ticket = ticket_response.json()

        quantity = ticket.get("quantity")
        event_id = ticket.get("event_id")

        # Get event details
        event_response = requests.get(f"http://127.0.0.1:8000/api/events/{event_id}/")
        if event_response.status_code != 200:
            raise serializers.ValidationError("Event not found")
        event = event_response.json()

        price = float(event.get("price", 0))
        available = int(event.get("available_tickets", 0))

        # Calculate total amount
        validated_data["amount"] = quantity * price
        validated_data["status"] = "paid"

        # Save the payment
        payment = super().create(validated_data)

        # Update available_tickets in event_service
        new_available = available - quantity
        if new_available < 0:
            raise serializers.ValidationError("Not enough tickets remaining to finalize payment.")

        update_data = {
            "organizer_id": event["organizer_id"],
            "title": event["title"],
            "description": event["description"],
            "location": event["location"],
            "date": event["date"],
            "price": event["price"],
            "available_tickets": new_available
        }

        update_response = requests.put(
            f"http://127.0.0.1:8000/api/events/{event_id}/",
            json=update_data
        )

        if update_response.status_code not in [200, 202]:
            raise serializers.ValidationError("Failed to update event ticket count")

        return payment
