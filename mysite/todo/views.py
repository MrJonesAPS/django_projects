from django.shortcuts import render
from django.views import generic

from .models import Item 

# Create your views here.
class IndexView(generic.ListView):
    model = Item
    


class DetailView(generic.DetailView):
    model = Item

