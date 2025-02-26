from django.shortcuts import render
from django.views import generic

from .models import Item 
from .forms import ItemForm
# Create your views here.
class IndexView(generic.ListView):
    model = Item
    


class DetailView(generic.DetailView):
    model = Item

class CreateView(generic.edit.CreateView):
    model = Item
    fields = '__all__'


