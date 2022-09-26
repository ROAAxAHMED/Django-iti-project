from django.shortcuts import render
from cars.forms import CarsModelForm
# Create your views here.
from cars.models import Cars
from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def CarsIndex(request):
    allcars = cars.get_all_books()
    return render(request, "cars/index.html", context={"cars":allcars})


class CarsDetails(DetailView):
    model = Cars
    template_name = "cars/show.html"


class CreateCarsView(CreateView):
    template_name = "Cars/create.html"
    form_class = CarsModelForm
    success_url = '/Cars/index'

class EditCarsView(UpdateView):
    template_name = "cars/edit.html"
    form_class = CarsModelForm
    success_url = '/cars/index'
    model = Cars



class DeleteCarsView(DeleteView):
    template_name = "cars/delete.html"
    model = Cars
    success_url = '/cars/index'
