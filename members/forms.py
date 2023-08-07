from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Extending Django standard forms by adding extra fields here.
# Standard Django forms can not be styled in html. Widgets makes bootstrap styling possible ('form-control' is a bootstrap class).
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
