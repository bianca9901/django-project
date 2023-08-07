from django.shortcuts import render, get_object_or_404, redirect
from .models import restaurant_event, restaurant_reservation
from .forms import ReservationForm

#Homepage
def home(request):
    return render(request, 'app_restaurant/home.html', {})


#Events page
def all_events(request): 
    event_list = restaurant_event.objects.all().order_by('event_date')
    return render(request, 'app_restaurant/restaurant_event_list.html',
    {'event_list': event_list})

# Start building reservation logic
def make_reservation(request, event_id):
    selected_event = get_object_or_404()


