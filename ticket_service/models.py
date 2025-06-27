from django.db import models
from event_service.models import Event
from django.contrib.auth.models import User

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.event.title} - {self.quantity} ticket(s)"
