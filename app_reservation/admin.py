from django.contrib import admin
from .models import restaurant_event
from .models import restaurant_user

admin.site.register(restaurant_event)
admin.site.register(restaurant_user)

