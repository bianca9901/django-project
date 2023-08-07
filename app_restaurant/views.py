from django.shortcuts import render
from .models import restaurant_event

#Homepage
def home(request):
    return render(request, 'app_restaurant/home.html', {})

#Events page
def all_events(request): 
    event_list = restaurant_event.objects.all().order_by('event_date')
    return render(request, 'app_restaurant/restaurant_event_list.html',
    {'event_list': event_list})


