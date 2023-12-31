from django import forms
from .models import restaurant_reservation, review


# Reservation form
class ReservationForm(forms.ModelForm):
    class Meta:
        model = restaurant_reservation
        fields = ['number_of_friends']



# Review form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['review_text']
