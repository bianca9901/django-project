from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_restaurant.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include ('members.urls')),
]

# Configure Admin Titles
admin.site.site_header = 'Restaurant Django Administration Page'
