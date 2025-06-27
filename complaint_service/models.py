from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    admin_response = models.TextField(blank=True)
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("responded", "Responded"),
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.id} from {self.full_name or self.user.get_full_name()}"
