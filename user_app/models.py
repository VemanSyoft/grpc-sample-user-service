from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000, blank=True, null=False)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=False)
    phone = models.CharField(max_length=1000, blank=True, null=False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.id)
