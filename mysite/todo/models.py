from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return "/todo/%i/" % self.id
