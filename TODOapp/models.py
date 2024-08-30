from django.db import models

class TODO(models.Model):
    TODO = models.CharField(max_length=200)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        return self.TODO


class Done(models.Model):
    original_todo = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.original_todo} - {"Deleted" if self.deleted else "Completed"}'
