from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

