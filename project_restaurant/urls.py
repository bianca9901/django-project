from django.contrib import admin
from django.urls import path, include
from app_restaurant.views import django_404, django_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_restaurant.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include ('members.urls')),
]

# Custom Error Pages
handler404 = django_404
handler500 = django_500

# Configure Admin Titles
admin.site.site_header = 'Restaurant Django Administration Page'
