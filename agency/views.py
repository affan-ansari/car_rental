from django.shortcuts import render,redirect
from django.contrib import messages
from .business_logic.agency import Agency
from .models import CAR
from .forms import RegisterCarForm,RegisterDriverForm

controller = Agency()

def home(request):
    context = {
        'cars': CAR.objects.all()
    }
    return render(request, 'agency/home.html', context)

def register_car(request):
    if request.method == 'POST':
        form = RegisterCarForm(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data.get("reg_no")
            make = form.cleaned_data.get("make")
            model = form.cleaned_data.get("model")
            body_type = form.cleaned_data.get("body_type")
            engine_capacity = form.cleaned_data.get("engine_capacity")
            seats = form.cleaned_data.get("seats")
            color = form.cleaned_data.get("color")
            transmission = form.cleaned_data.get("transmission")
            fuel = form.cleaned_data.get("fuel")

            controller.add_car(
                reg_no,make,model,body_type,engine_capacity,
                seats,color,transmission,fuel
            )
            messages.success(request, f'Car added successfully!')
            return redirect('agency-register-car')
    else:
        form = RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})

# def register_car(request):
#     if request.method == 'POST':
#         form = RegisterCarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Car added successfully!')
#             return redirect('agency-register-car')
#     else:
#         form = RegisterCarForm()
#     return render(request,'agency/register_car.html',{'form': form})

def register_driver(request):
    if request.method == 'POST':
        form = RegisterDriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Driver added successfully!')
            return redirect('agency-register-driver')
    else:
        form = RegisterDriverForm()
    return render(request,'agency/register_driver.html',{'form': form})
