from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .business_logic.agency import Agency
from .models import CAR,DRIVER
from .forms import RegisterCarForm,RegisterDriverForm,SearchCarForm,SearchDriverForm,DriverUpdateForm,CarUpdateForm

controller = Agency()

def home(request):
    context = {
        'cars': CAR.objects.all()
    }
    return render(request, 'agency/home.html', context)

def manage_cars(request):
    return render(request, 'agency/manage_cars.html')

def manage_drivers(request):
    return render(request, 'agency/manage_drivers.html')

class CarDetailView(DetailView):
    model = CAR

class DriverListView(ListView):
    model = DRIVER
    template_name= 'agency/drivers_list.html'
    context_object_name = 'drivers'

class DriverDetailView(DetailView):
     model = DRIVER

def register_car(request):
    if request.method == 'POST':
        form = RegisterCarForm(request.POST, request.FILES)
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
            image = form.cleaned_data.get("image")

            controller.add_car(
                reg_no,make,model,body_type,engine_capacity,
                seats,color,transmission,fuel,image
            )
            messages.success(request, f'Car added successfully!')
            return redirect('agency-register-car')
    else:
        form = RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})

def search_car(request):
    if request.method == 'POST':
        search_form = SearchCarForm(request.POST)
        if search_form.is_valid():
            reg_no = search_form.cleaned_data["reg_no"]
            try:
                searched_car = CAR.objects.get(reg_no=reg_no)
                messages.success(request, f'Car found!')
                return HttpResponseRedirect("car/{reg_no}/".format(reg_no= searched_car.reg_no))
            except ObjectDoesNotExist:
                messages.warning(request, f'Car not found!')
                return redirect('agency-search-car')
    else:
        search_form = SearchCarForm()
        return render(request,'agency/search_car.html',{'search_form': search_form})

def update_car(request,pk):
    searched_car = CAR.objects.get(reg_no=pk)
    print(searched_car.make)
    if request.method == 'POST':
        update_form = CarUpdateForm(request.POST, request.FILES, instance=searched_car)
        if update_form.is_valid():
            reg_no = update_form.cleaned_data.get("reg_no")
            make = update_form.cleaned_data.get("make")
            model = update_form.cleaned_data.get("model")
            body_type = update_form.cleaned_data.get("body_type")
            engine_capacity = update_form.cleaned_data.get("engine_capacity")
            seats = update_form.cleaned_data.get("seats")
            color = update_form.cleaned_data.get("color")
            transmission = update_form.cleaned_data.get("transmission")
            fuel = update_form.cleaned_data.get("fuel")
            image = update_form.cleaned_data.get("image")
            accident_details = update_form.cleaned_data.get("accident_details")
            available = update_form.cleaned_data.get("available")

            controller.update_car(reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image,accident_details,available)
            messages.success(request,f'Car Updated Succuessfully')
            return redirect('agency-home')
    else:
        update_form = CarUpdateForm(instance=searched_car)
        context = {'update_form': update_form}
        return render(request,'agency/update_car.html',context )

def delete_car(request):
    if request.method == 'POST':
        form = SearchCarForm(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data["reg_no"]
            is_deleted = controller.delete_car(reg_no)
            if is_deleted == True:
                messages.success(request, f'Car deleted successfully!')
            else:
                messages.info(request, f'Car does not exist!')
            return redirect ('agency-delete-car')
    else:
        form = SearchCarForm()
    return render(request,'agency/delete_car.html',{'form': form})

def register_driver(request):
    if request.method == 'POST':
        form = RegisterDriverForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data.get("CNIC")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            contact_number = form.cleaned_data.get("contact_number")
            address = form.cleaned_data.get("address")
            hourly_rate = form.cleaned_data.get("hourly_rate")

            controller.add_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)
            messages.success(request, f'Driver added successfully!')
            return redirect('agency-register-driver')
    else:
        form = RegisterDriverForm()
    return render(request,'agency/register_driver.html',{'form': form})

def update_driver(request):
    pass

def delete_driver(request):
    if request.method == 'POST':
        form = SearchDriverForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data["CNIC"]
            is_deleted = controller.delete_driver(CNIC)
            if is_deleted == True:
                messages.success(request, f'Driver deleted successfully!')
            else:
                messages.info(request, f'Driver does not exist!')
            return redirect ('agency-delete-driver')
    else:
        form = SearchDriverForm()
    return render(request,'agency/delete_driver.html',{'form': form})
