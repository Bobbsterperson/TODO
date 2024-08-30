from django.db import models


class TODO(models.Model):
    TODO = models.CharField(max_length=200)

    def __str__(self):
        return self.TODO
    

class DONE(models.Model):
    DONE = models.BooleanField(default=True)


