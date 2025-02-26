from django.urls import path

from . import views

app_name = "cosmo"
urlpatterns = [
    # ex: /cosmo/, show all timeslots
    path("", views.TimeslotIndexView.as_view(), name="index"),
    # ex: /cosmo/timeslot/5/, detail for one timeslot
    path("timeslot/<int:pk>/", views.TimeslotDetailView.as_view(), name="timeslot_detail"),
    path("appointment/<int:pk>/", views.AppointmentDetailView.as_view(), name="appointment_detail"),
]
