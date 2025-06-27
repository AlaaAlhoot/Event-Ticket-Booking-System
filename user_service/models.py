import string
import secrets
from django.db import models
from django.contrib.auth.models import User

def generate_secure_token(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('attendee', 'Attendee'),
        ('organizer', 'Organizer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    secure_token = models.CharField(
        max_length=64,
        unique=True,
        default=generate_secure_token,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_tickets_reserved = models.PositiveIntegerField(default=0)
    deleted_events_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role}"
