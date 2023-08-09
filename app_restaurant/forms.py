from django import forms
from .models import restaurant_reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = restaurant_reservation
        fields = ['num_friends']