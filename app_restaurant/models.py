from django.db import models
from django.contrib.auth.models import User



class restaurant_event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField('Event Date')
    employee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name