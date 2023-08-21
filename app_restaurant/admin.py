from django.contrib import admin
from .models import restaurant_event, restaurant_reservation, menu, review


# Inline display for event reservations
class ReservationInline(admin.TabularInline):
    model = restaurant_reservation
    extra = 0


# Registering the restaurant_event model
@admin.register(restaurant_event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'event_date', 'available_spots', 'description', 'image')
    list_display = ('name', 'event_date')
    list_filter = ('event_date',)
    ordering = ('-event_date',)
    inlines = [ReservationInline]


# Registering the menu model
@admin.register(menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'description', 'category')
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)


# Registering the review model
@admin.register(review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'review_text', 'pub_date')
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
