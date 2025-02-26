from django.shortcuts import render
from django.views import generic

from .models import Timeslot, Appointment
# Create your views here.
class TimeslotIndexView(generic.ListView):
    model = Timeslot

class TimeslotDetailView(generic.DetailView):
    model = Timeslot

class AppointmentDetailView(generic.DetailView):
    model = Appointment
