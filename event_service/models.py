from django.db import models
from django.contrib.auth.models import User
import secrets
import string
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    available_tickets = models.PositiveIntegerField(default=0)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=256, blank=True)  # optional digital signature
    secret_key = models.CharField(max_length=100, unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.secret_key:
            self.secret_key = self.generate_secret_key()
        super().save(*args, **kwargs)

    def generate_secret_key(self, length=50):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    @property
    def can_delete(self):

        time_passed = timezone.now() - self.created_at
        return time_passed.total_seconds() < 3 * 60 * 60

    def __str__(self):
        return f"{self.user.username} booked {self.quantity} for {self.event.title}"
