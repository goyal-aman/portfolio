from django.db import models
from timeline.models import Link
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=False, blank=False)
    end_date = models.DateField(default=timezone.now, null=False, blank=False)
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True)

    
    def __str__(self) -> str:
        return f"{self.heading}.. start: {self.start_date}, end:{self.end_date}"
