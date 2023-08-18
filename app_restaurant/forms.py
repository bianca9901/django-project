from django import forms
from .models import restaurant_reservation, review

class ReservationForm(forms.ModelForm):
    class Meta:
        model = restaurant_reservation
        fields = ['number_of_friends']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['review_text']