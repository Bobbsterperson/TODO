from django.db import models


class TODO(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    Notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']

