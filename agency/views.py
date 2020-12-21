from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView
from .business_logic.agency import Agency
from .models import CAR,DRIVER
from .forms import RegisterCarForm,RegisterDriverForm,DeleteCarForm,DeleteDriverForm,DriverUpdateForm

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

def delete_car(request):
    if request.method == 'POST':
        form = DeleteCarForm(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data["reg_no"]
            is_deleted = controller.delete_car(reg_no)
            if is_deleted == True:
                messages.success(request, f'Car deleted successfully!')
            else:
                messages.info(request, f'Car does not exist!')
            return redirect ('agency-delete-car')
    else:
        form = DeleteCarForm()
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

            controller.add_driver(CNIC,first_name,last_name,email,contact_number,address)
            messages.success(request, f'Driver added successfully!')
            return redirect('agency-register-driver')
    else:
        form = RegisterDriverForm()
    return render(request,'agency/register_driver.html',{'form': form})

def update_driver(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            search_form = DeleteDriverForm(request.POST)
            if search_form.is_valid():
                CNIC = search_form.cleaned_data["CNIC"]
                try:
                    searched_driver = DRIVER.objects.get(CNIC=CNIC)
                    update_form = DriverUpdateForm(instance=searched_driver)
                    context = {
                        'update_form': update_form,
                        'searched': True,
                    }
                    messages.success(request, f'Driver found!')
                    return render(request,'agency/update_driver.html',context)
                except ObjectDoesNotExist:
                    messages.warning(request, f'Driver not found!')
                    return redirect('agency-update-driver')

        elif 'update' in request.POST:
            update_form = DriverUpdateForm(request.POST)
            if update_form.is_valid():
                CNIC = update_form.cleaned_data.get("CNIC")
                first_name = update_form.cleaned_data.get("first_name")
                last_name = update_form.cleaned_data.get("last_name")
                email = update_form.cleaned_data.get("email")
                contact_number = update_form.cleaned_data.get("contact_number")
                address = update_form.cleaned_data.get("address")

                controller.update_driver(CNIC,first_name,last_name,email,contact_number,address)
                messages.success(request, f"Driver was updated!")
                return redirect('agency-update-driver')
    else:
        search_form = DeleteDriverForm()
        context = {
            'search_form': search_form,
            'searched': False,
        }
        return render(request,'agency/update_driver.html',context)

def delete_driver(request):
    if request.method == 'POST':
        form = DeleteDriverForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data["CNIC"]
            is_deleted = controller.delete_driver(CNIC)
            if is_deleted == True:
                messages.success(request, f'Driver deleted successfully!')
            else:
                messages.info(request, f'Driver does not exist!')
            return redirect ('agency-delete-driver')
    else:
        form = DeleteDriverForm()
    return render(request,'agency/delete_driver.html',{'form': form})


# def register_driver(request):
#     if request.method == 'POST':
#         form = RegisterDriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Driver added successfully!')
#             return redirect('agency-register-driver')
#     else:
#         form = RegisterDriverForm()
#     return render(request,'agency/register_driver.html',{'form': form})
