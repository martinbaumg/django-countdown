from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:show-event', kwargs={'id': self.id})