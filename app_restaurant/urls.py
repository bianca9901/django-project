from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.all_events, name='list-events'),
    path('make_reservation/<int:event_id>/', views.make_reservation, name='make_reservation'),
    path('reservation_form/<int:event_id>/', views.reservation_form, name='reservation_form'),
    path('my_events/', views.my_events, name='my_events'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
]