from django.db import models 
from django.utils import timezone

class Link(models.Model):
    url = models.URLField()
    name = models.CharField(default="", null=True, blank=True, max_length=999)

    def __str__(self):
        return self.url

class Card(models.Model):
    """
    In timeline: Each achievement is shown in card
    """
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    date = models.DateField(default=timezone.now, null=False, blank=False)
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.heading}.. on {self.date}"