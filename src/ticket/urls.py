from django.urls import path

from . import views

app_name = "ticket"
urlpatterns = [
    path('list/', views.TicketListView.as_view(), name='ticket_list'),
    path('detail/<slug:slug>', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('create/', views.TicketCreateView.as_view(), name='ticket_create'),
]