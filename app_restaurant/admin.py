from django.contrib import admin
from .models import restaurant_event


@admin.register(restaurant_event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'event_date', 'description', 'employee')
    list_display = ('name', 'event_date')
    list_filter = ('event_date',)
    ordering = ('-event_date',)