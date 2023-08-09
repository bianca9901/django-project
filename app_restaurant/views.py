from django.shortcuts import render, get_object_or_404, redirect
from .models import restaurant_event, restaurant_reservation
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Homepage
def home(request):
    return render(request, 'app_restaurant/home.html', {})


#Events page
def all_events(request): 
    event_list = restaurant_event.objects.all().order_by('event_date')
    return render(request, 'app_restaurant/restaurant_event_list.html',
    {'event_list': event_list})


# Reservation
@login_required(login_url='login')
def make_reservation(request, event_id):
    return redirect('reservation_form', event_id=event_id)


@login_required(login_url='login')
def reservation_form(request, event_id):
    selected_event = get_object_or_404(restaurant_event, pk=event_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.event = selected_event
            reservation.user = request.user

            total_spots_needed = reservation.num_friends + 1

            remaining_spots = selected_event.available_spots - total_spots_needed

            if remaining_spots >= 0:
                reservation.save()
                selected_event.available_spots = remaining_spots
                selected_event.save()

                messages.success(request, 'Reservation successfully submitted!')
                return redirect('my_events')
            else:
                messages.error(request, 'Sorry, there are no more available spots for this event.')
                return redirect('list-events')

    else:
        form = ReservationForm()

    return render(request, 'app_restaurant/reservation_form.html', {'selected_event': selected_event, 'form': form})


#My Events Page
@login_required(login_url='login')
def my_events(request):
    user = request.user
    user_reservations = restaurant_reservation.objects.filter(user=user).select_related('event')
    events = [{'event': reservation.event, 'reservation': reservation} for reservation in user_reservations]

    return render(request, 'app_restaurant/my_events.html', {'events': events})
