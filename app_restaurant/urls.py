from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.all_events, name='list-events'),
    path('make_reservation/<int:event_id>/', views.make_reservation, name='make_reservation'),
    path('reservation_form/<int:event_id>/', views.reservation_form, name='reservation_form'),
]