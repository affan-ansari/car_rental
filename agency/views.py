from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .business_logic.rental_agency import car_list
from .forms import RegisterCarForm

def home(request):
    context = {
        'cars': car_list()
    }
    return render(request, 'agency/base.html', context)

def register_car(request):
    if request.method == 'POST':
        form = RegisterCarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})