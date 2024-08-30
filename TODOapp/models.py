from django.db import models

class TODO(models.Model):
    TODO = models.CharField(max_length=200)

class DONE(models.Model):
    DONE = models.BooleanField(default=False)


