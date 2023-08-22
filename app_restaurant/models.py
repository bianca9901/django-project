from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class restaurant_event(models.Model):
    """´
    Represents details about the event.
    """
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField('Event Date')
    description = models.TextField(blank=True)
    available_spots = models.PositiveIntegerField(default=30)
    image = models.ImageField('image', blank=True)

    def __str__(self):
        return self.name

    @property
    def calculate_available_spots(self):
        """
        Calculates the number of available spots for the event,
        considering existing reservations.
        """
        reserved_spots = sum(
            reservation.number_of_friends + 1
            for reservation in self.reservations.all())
        available_spots = self.available_spots - reserved_spots
        return max(available_spots, 0)


class restaurant_reservation(models.Model):
    """
    Represents a reservation for an event by a user.
    """
    number_of_friends = models.PositiveIntegerField(
                                 default=0, validators=[MaxValueValidator(30)])
    event = models.ForeignKey(
        restaurant_event,
        on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation for {self.user} at {self.event}"


class menu(models.Model):
    """
    Represents a menu item, that is in the category of food or drinks,
    and details about the item.
    """
    FOOD = 'food'
    DRINKS = 'drinks'
    CATEGORY_CHOICES = [
        (FOOD, 'Food'),
        (DRINKS, 'Drinks'),
    ]

    name = models.CharField('Item Name', max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default=FOOD)

    def __str__(self):
        return self.name


class review(models.Model):
    """
    Represents a review by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.pub_date}"
