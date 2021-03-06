from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

    def toggle(self):
        self.completed = not self.completed
        if self.completed:
            self.completed_date = timezone.now()
        else:
            self.completed_date = None
        self.save()
