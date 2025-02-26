from django.db import models

# Create your models here.
class Timeslot(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
