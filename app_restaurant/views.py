from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import restaurant_event, restaurant_reservation
from .forms import ReservationForm

def home(request):
    """ Home page:
Functionality: Displays home page. Returns: Home template. """
    return render(request, 'app_restaurant/home.html', {})


def menu(request):
    """ Menu page:
Functionality: Displays menu page. Returns: Menu template. """
    return render(request, 'app_restaurant/menu.html', {})


def about_us(request):
    """ About us page:
Functionality: Displays about us page. Returns: About us template. """
    return render(request, 'app_restaurant/about_us.html', {})


def all_events(request):
    """ Events list page:
Functionality:
- Retrieves events and pictures that was made by the staff in the Admin Dashboard.
How it works:
- Queries the database for all restaurant events.
- Retrieves event detials, including available spots.
Returns: Rendered event list template. """
    event_list = restaurant_event.objects.all().order_by('event_date')
    for event in event_list:
        event.available_spots
    context = {'event_list': event_list}
    return render(request, 'app_restaurant/restaurant_event_list.html', context)


@login_required(login_url='login')
def make_reservation(request, event_id):
    """ Reservation form page:
Functionality:
- Redirects user to the reservation form for a specific event.
How it works:
-Retrieves event ID from the url.
Returns: redirects user to the reservation_form template. """
    return redirect('reservation_form', event_id=event_id)


@login_required(login_url='login')
def reservation_form(request, event_id):
    """ Reservation form (Logic):
Functionality:
- Handles the logic for making a reservation for a specific event.
How it works:
- Retrieves the selected event based on event id from url.
- Checks if user already has reservation for this event. If reservation already exists, a message displays.
- If user do not have reservation for this event:
  1. Form data is validated.
  2. New reservation is created.
  3. Checks if there are available spots for this event.
  4. If available spots: reservation is saved, if not, a message displays.
Returns: rendered reservation form template. """
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
                return redirect('list_events')
            else:
                messages.error(request, 'Sorry, there are no more available spots for this event.')
                return redirect('list_events')
    else:
        form = ReservationForm()

    return render(request, 'app_restaurant/reservation_form.html', {'selected_event': selected_event, 'form': form})


@login_required(login_url='login')
def my_events(request):
    """ My Events page (General)
Functionality:
- Displays events reserved by the currently logged in user.
- How it works: Retrieves reservations made by the user and events' details.
Returns: Rendered my Events template. """
    user_reservations = restaurant_reservation.objects.filter(user=request.user).select_related('event')
    events = [{'event': reservation.event, 'reservation': reservation} for reservation in user_reservations]
    return render(request, 'app_restaurant/my_events.html', {'events': events})


@login_required(login_url='login')
def cancel_reservation(request, reservation_id):
    """ My Events page (Cancel):
Functionality:
- If Cancel reservation = POST:
- Spots reserved for this event gets added back to the available spots for the event.
- Reservation is deleted.
- User gets notified with message.
How it works: Variables saving the reservation details, such as username that made booking gets deleted.
And number of friends + user total is restored to available spots sum.
Returns: Rendered my Events template. """
    reservation = get_object_or_404(restaurant_reservation, pk=reservation_id, user=request.user)
    selected_event = reservation.event

    if request.method == 'POST':
        total_spots_freed = reservation.number_of_friends + 1
        selected_event.available_spots += total_spots_freed
        selected_event.save()
        reservation.delete()
        messages.success(request, 'Your reservation was canceled!')
        return redirect('my_events')

    return render(request, 'app_restaurant/my_events.html', {'selected_event': selected_event})


@login_required(login_url='login')
def edit_reservation(request, reservation_id):
    """ My Events page (Edit):
Functionality:
- If Edit reservation = POST:
- Spots reserved for this event gets added back to the available spots for the event.
- Reservation is deleted.
- User gets notified with message.
- User is redirected to the particular event they wanted to edit.
How it works: Variables saving the reservation details, such as username that made booking gets deleted.
And number of friends + user total is restored to available spots sum. The event id is used to redirect
user to the particular event they wanted to make a updated decision on reservation details for.
Returns: Rendered my Events template. """
    reservation = get_object_or_404(restaurant_reservation, pk=reservation_id, user=request.user)
    selected_event = reservation.event

    if request.method == 'POST':
        total_spots_freed = reservation.number_of_friends + 1
        selected_event.available_spots += total_spots_freed
        selected_event.save()
        reservation.delete()
        messages.success(request, 'Your reservation was canceled. You can now make a new reservation.')
        return redirect('reservation_form', event_id=selected_event.id)
    return render(request, 'app_restaurant/my_events.html', {'selected_event': selected_event})
