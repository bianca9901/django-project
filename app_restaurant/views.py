from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import restaurant_event, restaurant_reservation, menu, review
from .forms import ReservationForm, ReviewForm


def home(request):
    return render(request, 'app_restaurant/home.html', {})


def about_us(request):
    return render(request, 'app_restaurant/about_us.html', {})


def display_menu(request):
    """Queries the database for all menu items categorized
    as 'food' and 'drinks'."""
    food_items = menu.objects.filter(category='food')
    drinks_items = menu.objects.filter(category='drinks')
    context = {'food_items': food_items, 'drinks_items': drinks_items}
    return render(request, 'app_restaurant/menu.html', context)


def all_events(request):
    """Queries the database for all events and orders them
    by date, also retrieves the available spots."""
    event_list = restaurant_event.objects.all().order_by('event_date')
    for event in event_list:
        event.available_spots
    context = {'event_list': event_list}
    return render(request, 'app_restaurant/restaurant_event_list.html', context)


@login_required(login_url='login')
def make_reservation(request, event_id):
    """Redirects user to the reservation form for a specific
    event."""
    return redirect('reservation_form', event_id=event_id)


@login_required(login_url='login')
def reservation_form(request, event_id):
    """Handles the logic for making a reservation for a specific event.
1. Retrieves the selected event.
2. Checks if user already has a reservation for this event. If reservation
already exists, the user is redirected.
3. If the user do not already have a reservation for this event:
- The reservation gets saved. Which makes it possible for the variable
total_spots_needed to hold the user (user-account), and the user (1) +
the number of friends (x) = sum.
The sum then gets compared to the events current available spots.
If the sum is less than or equal to the available spots, it means the reservation
can be done. The selected_event variable then saves this data to it."""
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
        form = ReservationForm()
    context = {'selected_event': selected_event, 'form': form}
    return render(request, 'app_restaurant/reservation_form.html', context)


@login_required(login_url='login')
def my_events(request):
    """Queries the database to fetch reservations associated
    with the user."""
    user_reservations = restaurant_reservation.objects.filter(user=request.user).select_related('event')
    events = [{'event': reservation.event, 'reservation': reservation} for reservation in user_reservations]
    context = {'events': events}
    return render(request, 'app_restaurant/my_events.html', context)


@login_required(login_url='login')
def cancel_reservation(request, reservation_id):
    """
1. The spots user reserved for this event is put into the
total_spots_freed variable and gets restored to the events available spots.
2. Reservation is deleted."""
    reservation = get_object_or_404(restaurant_reservation, pk=reservation_id, user=request.user)
    selected_event = reservation.event

    if request.method == 'POST':
        total_spots_freed = reservation.number_of_friends + 1
        selected_event.available_spots += total_spots_freed
        selected_event.save()
        reservation.delete()
        messages.success(request, 'Your reservation was canceled!')
        return redirect('my_events')
    context = {'selected_event': selected_event}
    return render(request, 'app_restaurant/my_events.html', context)


@login_required(login_url='login')
def edit_reservation(request, reservation_id):
    """
1. The spots user reserved for this event is put into the
total_spots_freed variable and gets restored to the events available spots.
2. Reservation is deleted.
3. User is redirected to the particular event they wanted to edit."""
    reservation = get_object_or_404(restaurant_reservation, pk=reservation_id, user=request.user)
    selected_event = reservation.event

    if request.method == 'POST':
        total_spots_freed = reservation.number_of_friends + 1
        selected_event.available_spots += total_spots_freed
        selected_event.save()
        reservation.delete()
        messages.success(request, 'Your reservation was canceled. You can now make a new reservation.')
        return redirect('reservation_form', event_id=selected_event.id)
    context = {'selected_event': selected_event}
    return render(request, 'app_restaurant/my_events.html', context)


def list_reviews(request):
    """Queries the database for all reviews."""
    reviews = review.objects.all().order_by('-pub_date')
    context = {'reviews': reviews}
    return render(request, 'app_restaurant/list_reviews.html', context)


@login_required(login_url='login')
def post_review(request):
    """Allows users to submit reviews, handles form validation and user
    association."""
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has successfully been submitted! Thank you for taking your time.')
            return redirect('list_reviews')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'app_restaurant/post_review.html', context)


@login_required(login_url='login')
def edit_review(request, review_id):
    """Allows user to edit their review. Form is prepopulated with
    their previous review text."""
    review_to_edit = get_object_or_404(review, pk=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review_to_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has successfully been edited! Thank you for taking your time.')
            return redirect('list_reviews')
    else:
        form = ReviewForm(instance=review_to_edit)
    context = {'form': form, 'review': review_to_edit}
    return render(request, 'app_restaurant/edit_review.html', context)


@login_required(login_url='login')
def delete_review(request, review_id):
    """Allows user to delete their review."""
    review_to_delete = get_object_or_404(review, pk=review_id, user=request.user)
    if request.method == 'POST':
        review_to_delete.delete()
        messages.success(request, 'Your review was deleted!')
        return redirect('list_reviews')


def django_404(request, exception):
    """Custom error 404 page"""
    return render(request, 'app_restaurant/errors/404.html', status=404)


def django_500(request):
    """Custom error 500 page"""
    return render(request, 'app_restaurant/errors/500.html', status=500)
