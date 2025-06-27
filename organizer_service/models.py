from django.db import models

class Organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    org_name = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.org_name} (Verified: {self.verified})"
