from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name