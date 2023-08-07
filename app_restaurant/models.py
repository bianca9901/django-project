from django.db import models
from django.contrib.auth.models import User

class restaurant_event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField('Event Date')
    employee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class restaurant_reservation(models.Model):
    event = models.ForeignKey(restaurant_event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solo = models.BooleanField(default=True)
    num_friends = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Reservation for {self.user} at {self.event}"