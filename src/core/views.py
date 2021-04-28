from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from ticket.models import Ticket

def home(request):
    wating = Ticket.objects.filter(status='In asteptare')[:5]
    working_on_it = Ticket.objects.filter(status='In lucru')[:5]
    finished = Ticket.objects.filter(status='Terminate')[:5]

    return render(request, 'index.html', {'wating': wating, 'working_on_it':working_on_it, 'finished':finished})