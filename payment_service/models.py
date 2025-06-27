from django.db import models
from django.contrib.auth.models import User
from event_service.models import Event


class PaymentCard(models.Model):
    CARD_TYPE_CHOICES = [
        ('Visa', 'Visa'),
        ('Mastercard', 'Mastercard'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
    expiry_month = models.CharField(max_length=2)
    expiry_year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.card_holder} ({self.card_type})"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_id = models.IntegerField()  # Reference to Ticket ID from ticket_service
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"💰 Payment by {self.user.get_full_name()} - ${self.amount}"
