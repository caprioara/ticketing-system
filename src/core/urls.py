from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ticket/', include('ticket.urls', namespace='ticket')),
    path('account/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
