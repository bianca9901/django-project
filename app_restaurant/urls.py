from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.all_events, name='list_events'),
    path('make_reservation/<int:event_id>/', views.make_reservation, name='make_reservation'),
    path('reservation_form/<int:event_id>/', views.reservation_form, name='reservation_form'),
    path('my_events/', views.my_events, name='my_events'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('menu', views.display_menu, name='menu'),
    path('about_us', views.about_us, name='about_us'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('list_reviews/', views.list_reviews, name='list_reviews'),
    path('post_review/', views.post_review, name='post_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]