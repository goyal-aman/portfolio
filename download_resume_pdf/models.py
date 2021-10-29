from django.db import models

# Create your models here.
class ResumeLink(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: there should only be one active resume at a time.
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # unset is_active of all other resume to false,
        
        if self.is_active:
            activeResumes = ResumeLink.objects.filter(is_active=True)
            for resume in activeResumes:
                resume.is_active = False
            ResumeLink.objects.bulk_update(activeResumes, ['is_active'])
        super(ResumeLink, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name[:30]}.. url:{self.url[:30]}"
