from django.db import models 
from django.utils import timezone

class Card(models.Model):
    """
    In timeline: Each achievement is shown in card
    """
    text = models.TextField(max_length=999, default="", null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.text[:20]}.. on {self.date}"