from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import restaurant_event, restaurant_reservation
from .forms import ReservationForm

@login_required(login_url='login')
#Homepage
def home(request):
    return render(request, 'app_restaurant/home.html', {})

@login_required(login_url='login')
#Events list page
def all_events(request):
    event_list = restaurant_event.objects.all().order_by('event_date')
    for event in event_list:
        event.available_spots
    return render(request, 'app_restaurant/restaurant_event_list.html', {'event_list': event_list})

@login_required(login_url='login')
#Reservation form page
def make_reservation(request, event_id):
    return redirect('reservation_form', event_id=event_id)

@login_required(login_url='login')
#Reservation form logic
def reservation_form(request, event_id):
    selected_event = get_object_or_404(restaurant_event, pk=event_id)
    user = request.user
    existing_reservation = restaurant_reservation.objects.filter(user=user, event=selected_event).first()

    if existing_reservation:
        messages.info(request, 'You have already reserved your spot for this event!')
        return redirect('my_events')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.event = selected_event
            reservation.user = user
            total_spots_needed = reservation.number_of_friends + 1

            if selected_event.available_spots >= total_spots_needed:
                reservation.save()
                selected_event.available_spots -= total_spots_needed
                selected_event.save()
                messages.success(request, 'Reservation successfully submitted!')
                return redirect('list-events')
            else:
                messages.error(request, 'Sorry, there are no more available spots for this event.')
                return redirect('list-events')
    else:
        form = ReservationForm()

    return render(request, 'app_restaurant/reservation_form.html', {'selected_event': selected_event, 'form': form})

@login_required(login_url='login')
#My Events page
def my_events(request):
    user_reservations = restaurant_reservation.objects.filter(user=request.user).select_related('event')
    events = [{'event': reservation.event, 'reservation': reservation} for reservation in user_reservations]
    return render(request, 'app_restaurant/my_events.html', {'events': events})

@login_required(login_url='login')
#Cancel reservation logic
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(restaurant_reservation, pk=reservation_id, user=request.user)
    selected_event = reservation.event

    if request.method == 'POST':
        total_spots_needed = reservation.number_of_friends + 1
        selected_event.available_spots += total_spots_needed
        selected_event.save()
        reservation.delete()
        messages.success(request, 'Your reservation was canceled!')
        return redirect('my_events')

    return render(request, 'app_restaurant/my_events.html', {'selected_event': selected_event})
