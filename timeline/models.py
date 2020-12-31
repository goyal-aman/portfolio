from django.db import models 
from django.utils import timezone

class Card(models.Model):
    """
    In timeline: Each achievement is shown in card
    """
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    date = models.DateField(default=timezone.now, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.body[:20]}.. on {self.date}"