from django.db import models

class restaurant_user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class restaurant_event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField('Event Date')
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(restaurant_user, blank=True)

    def __str__(self):
        return self.name