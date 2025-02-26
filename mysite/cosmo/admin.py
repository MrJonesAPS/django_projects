from django.contrib import admin

from .models import Timeslot, Appointment
# Register your models here.
admin.site.register(Timeslot)
admin.site.register(Appointment)
