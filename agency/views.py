from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .business_logic.agency import Agency
from .models import CAR,DRIVER,BOOKING,RENTAL
# from .forms import RegisterCarForm,RegisterDriverForm,SearchCarForm,SearchDriverForm,DriverUpdateForm,CarUpdateForm
from . import forms

controller = Agency()

def home(request):
    context = {
        'cars': controller.cars.get_cars()#Cars which are not deleted.
    }
    return render(request, 'agency/home.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_cars(request):
    return render(request, 'agency/manage_cars.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
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

class BookingsDetailsView(DetailView):
     model = BOOKING

class RentalsDetailsView(DetailView):
     model = RENTAL

@login_required
def BookingsView(request):
    bookings = controller.bookings.get_bookings(request.user)
    rentals = RENTAL.objects.all() #if superuser
    # for booking in bookings:
    #     tempvar = RENTAL.objects.get(booking=booking)
    #     rentals = RENTAL.objects.filter(
    #         Q(booking_id = tempvar.id)
    #         )
    # bookings = BOOKING.objects.filter(
    #     Q(is_driver_needed=True) & Q(allocated_car_id='ARX-33Y')
    # )
    rentalsExist = rentals.exists()
    context = {'bookings':bookings,'rentals':rentals,'rentalsExist':rentalsExist}
    return render(request, 'agency/bookings_list.html',context)

@login_required
def RentalsView(request):
    rentals = RENTAL.objects.all()
    context = {'rentals':rentals}
    return render(request,'agency/rentals_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_car(request):
    if request.method == 'POST':
        form = forms.RegisterCarForm(request.POST, request.FILES)
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
        form = forms.RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})

def search_car(request):
    if request.method == 'POST':
        search_form = forms.SearchCarForm(request.POST)
        if search_form.is_valid():
            reg_no = search_form.cleaned_data["reg_no"]
            try:
                searched_car = controller.cars.get_car(reg_no)
                messages.success(request, f'Car found!')
                return HttpResponseRedirect("car/{reg_no}/".format(reg_no= searched_car.reg_no))
            except Exception as exc:
                messages.warning(request, f'{exc}')
                return redirect('agency-search-car')
    else:
        search_form = forms.SearchCarForm()
        return render(request,'agency/search_car.html',{'search_form': search_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_car(request,pk):
    searched_car = CAR.objects.get(reg_no=pk)
    if request.method == 'POST':
        update_form = forms.CarUpdateForm(request.POST, request.FILES, instance=searched_car)
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
        update_form = forms.CarUpdateForm(instance=searched_car)
        context = {'update_form': update_form}
        return render(request,'agency/update_car.html',context )

@login_required
@user_passes_test(lambda u: u.is_superuser)
def search_driver(request):
    if request.method == 'POST':
        search_form = forms.SearchDriverForm(request.POST)
        if search_form.is_valid():
            CNIC = search_form.cleaned_data["CNIC"]
            try:
                searched_driver = controller.drivers.get_driver(CNIC)
                messages.success(request, f'Driver found!')
                return HttpResponseRedirect("driver/{CNIC}/".format(CNIC= searched_driver.CNIC))
            except Exception as exc:
                messages.warning(request, f'{exc}')
                return redirect('agency-search-driver')
    else:
        search_form = forms.SearchDriverForm()
        return render(request,'agency/search_driver.html',{'search_form': search_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_driver(request,pk):
    searched_driver = DRIVER.objects.get(CNIC=pk )
    if request.method == 'POST':
        update_form = forms.DriverUpdateForm(request.POST, instance=searched_driver)
        if update_form.is_valid():
            CNIC = update_form.cleaned_data.get("CNIC")
            first_name = update_form.cleaned_data.get("first_name")
            last_name = update_form.cleaned_data.get("last_name")
            email = update_form.cleaned_data.get("email")
            contact_number = update_form.cleaned_data.get("contact_number")
            address = update_form.cleaned_data.get("address")
            hourly_rate = update_form.cleaned_data.get("hourly_rate")

            controller.update_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate )
            messages.success(request,f'Driver Updated Succuessfully')
            return redirect('agency-home')
    else:
        update_form = forms.DriverUpdateForm(instance=searched_driver)
        context = {'update_form': update_form}
        return render(request,'agency/update_driver.html',context )

@login_required
@user_passes_test(lambda u: u.is_superuser == False)
def book_car(request,pk):
    selected_car = CAR.objects.get(reg_no=pk)
    if request.method == 'POST':
        book_form = forms.BookCarForm(request.POST)
        if book_form.is_valid():
            allocated_car = selected_car
            start_date_time= book_form.cleaned_data.get("start_date_time")
            end_date_time= book_form.cleaned_data.get("end_date_time")
            pickup_location= book_form.cleaned_data.get("pickup_location")
            is_driver_needed= book_form.cleaned_data.get("is_driver_needed")
            customer = request.user
            try:
                controller.book_car(customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed)
            except Exception as exc:
                messages.warning(request,f'{exc}')
                return redirect('agency-book-car',pk)
            #Put try except for Exception (if date time not available driver).
            messages.success(request,f'Car Booked Successfully')
            return redirect('car-detail',pk)
        else:
            messages.warning(request,f'Validation error')
            return redirect('agency-book-car',pk)

    else:
        book_form = forms.BookCarForm()
        # book_form = forms.BookCarForm(instance = selected_car)
        context = {
            'car': selected_car,
            'book_form': book_form
        }
        return render(request,'agency/book_car.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_car(request):
    if request.method == 'POST':
        form = forms.SearchCarForm(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data["reg_no"]
            is_deleted = controller.delete_car(reg_no)
            if is_deleted == True:
                messages.success(request, f'Car deleted successfully!')
            else:
                messages.info(request, f'Car does not exist!')
            return redirect ('agency-delete-car')
    else:
        form = forms.SearchCarForm()
    return render(request,'agency/delete_car.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_driver(request):
    if request.method == 'POST':
        form = forms.RegisterDriverForm(request.POST)
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
        form = forms.RegisterDriverForm()
    return render(request,'agency/register_driver.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_driver(request):
    if request.method == 'POST':
        form = forms.SearchDriverForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data["CNIC"]
            is_deleted = controller.delete_driver(CNIC)
            if is_deleted == True:
                messages.success(request, f'Driver deleted successfully!')
            else:
                messages.info(request, f'Driver does not exist!')
            return redirect ('agency-delete-driver')
    else:
        form = forms.SearchDriverForm()
    return render(request,'agency/delete_driver.html',{'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def receive_car(request,pk):
    selected_booking = BOOKING.objects.get(id=pk)
    if request.method == 'POST':
        rental_form = forms.RentalCarForm(request.POST)
        if rental_form.is_valid():
            allocated_booking = selected_booking
            date_of_delivery = rental_form.cleaned_data.get("date_of_delivery")
            try:
                controller.receive_car(allocated_booking,date_of_delivery)
            except Exception as exc:
                messages.warning(request,f'{exc}')
                return redirect('agency-receive-car',pk)
            messages.success(request,f'Car Delivered Successfully!')
            return redirect('agency-receive-car',pk)
        else:
            messages.warning(request,f'Validation error')
            return redirect('agency-receive-car',pk)

    else:
        rental_form = forms.RentalCarForm()
        context = {
            'booking': selected_booking,
            'rental_form': rental_form
        }
        return render(request,'agency/receive_car.html',context)

