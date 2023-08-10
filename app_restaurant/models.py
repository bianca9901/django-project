from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class restaurant_event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField('Event Date')
    description = models.TextField(blank=True)
    available_spots = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name

    @property
    def calculate_available_spots(self):
        reserved_spots = sum(reservation.number_of_friends + 1 for reservation in self.reservations.all())
        available_spots = self.available_spots - reserved_spots
        return max(available_spots, 0)

class restaurant_reservation(models.Model):
    event = models.ForeignKey(restaurant_event, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_friends = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(30)])

    def __str__(self):
        return f"Reservation for {self.user} at {self.event}"
