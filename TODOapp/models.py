from django.db import models
from ckeditor.fields import RichTextField


class TODO(models.Model):
    TODO = models.CharField(max_length=200, null=True, blank=True)
    Notes = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.TODO


class Done(models.Model):
    original_todo = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    Notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.original_todo} - {"Deleted" if self.deleted else "Completed"}'
