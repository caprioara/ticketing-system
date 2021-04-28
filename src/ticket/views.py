from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Ticket
from .forms import TicketForm


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'
    context_object_name = 'ticketdetail'

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'
    context_object_name = 'ticketlist'

class TicketCreateView(CreateView):
    form_class = TicketForm
    template_name = 'ticket/ticket_create.html'



