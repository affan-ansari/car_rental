from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Car
from .business_logic.rental_agency import car_list
from .forms import RegisterCarForm

def home(request):
    context = {
        'cars': car_list()
    }
    return render(request, 'agency/home.html', context)

def register_car(request):
    if request.method == 'POST':
        form = RegisterCarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Car added successfully!')
            return redirect('agency-register-car')
    else:
        form = RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})