from django.db import models

# Create your models here.
class ResumePdfLink(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=False, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} @ {self.link[:30]}.. created_on{self.created_date}"
