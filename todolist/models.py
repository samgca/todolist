from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    note_text = models.TextField(max_length=2500, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    status = models.BooleanField(default=False)
