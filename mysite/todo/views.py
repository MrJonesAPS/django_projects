from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
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
    success_url = reverse_lazy("todo:index")

class UpdateView(generic.edit.UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy("todo:index")

class DeleteView(generic.edit.DeleteView):
    model = Item
    success_url = reverse_lazy("todo:index")
