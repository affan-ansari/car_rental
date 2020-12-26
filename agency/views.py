from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .business_logic.agency import Agency
from .models import CAR, CREDIT_CARD,DRIVER,BOOKING,RENTAL,CAR_MODEL,PAYMENT,INVOICE,LATEFINE,DAMAGES,FINES
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
    context = {'bookings':bookings}
    return render(request, 'agency/bookings_list.html',context)

@login_required
def RentalsView(request):
    rentals = controller.rentals.get_rentals(request.user)
    context = {'rentals':rentals}
    return render(request,'agency/rentals_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_car(request):
    if request.method == 'POST':
        form = forms.RegisterCarForm(request.POST, request.FILES)
        if form.is_valid():
            car_model = form.cleaned_data.get("car_model")
            reg_no = form.cleaned_data.get("reg_no")
            color = form.cleaned_data.get("color")
            fuel = form.cleaned_data.get("fuel")
            image = form.cleaned_data.get("image")
            fare = form.cleaned_data.get("fare")

            controller.add_car(car_model,reg_no,color,fuel,fare,image)
            messages.success(request, f'Car added successfully!')
            return redirect('agency-register-car')
    else:
        form = forms.RegisterCarForm()
    return render(request,'agency/register_car.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_carmodel(request):
    if request.method == 'POST':
        form = forms.RegisterCarModelForm(request.POST)
        if form.is_valid():
            make = form.cleaned_data.get("make")
            model = form.cleaned_data.get("model")
            body_type = form.cleaned_data.get("body_type")
            engine_capacity = form.cleaned_data.get("engine_capacity")
            seats = form.cleaned_data.get("seats")
            transmission = form.cleaned_data.get("transmission")
            controller.add_carmodel(make,model,body_type,engine_capacity,seats,transmission)
            messages.success(request, f'Car Model added successfully!')
            return redirect('agency-register-carmodel')
    else:
        form = forms.RegisterCarModelForm()
    return render(request,'agency/register_carmodel.html',{'form': form})

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
    searched_car = controller.cars.get_car(pk)
    if request.method == 'POST':
        update_form = forms.CarUpdateForm(request.POST, request.FILES, instance=searched_car)
        if update_form.is_valid():
            color = update_form.cleaned_data.get("color")
            fuel = update_form.cleaned_data.get("fuel")
            image = update_form.cleaned_data.get("image")
            accident_details = update_form.cleaned_data.get("accident_details")
            fare = update_form.cleaned_data.get("fare")

            controller.update_car(searched_car,color,fuel,image,fare,accident_details)
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
    searched_driver = controller.drivers.get_driver(pk)
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
    selected_car = controller.cars.get_car(pk)
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
                new_booking = controller.book_car(customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed)
            except Exception as exc:
                messages.warning(request,f'{exc}')
                return redirect('agency-book-car',pk)
            #Put try except for Exception (if date time not available driver).
            messages.success(request,f'Car Booked Successfully')
            return redirect('agency-create-invoice',new_booking.id)
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
    selected_booking = controller.bookings.get_booking(pk)
    selected_invoice = controller.invoices.get_invoice(pk)
    if selected_invoice.payment == None:
        messages.warning(request,f'Payment corresponding to Invoice ID: {selected_invoice.id} has not been made!')
        return redirect('agency-bookings-list')
    else:
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

@login_required
def create_invoice(request,pk):
    try:
        invoice = controller.create_invoice(pk)
        context = {
            'invoice': invoice,
        }
        return render(request,'agency/invoice_detail.html',context)
    except:
        try:
            invoice = controller.invoices.get_invoice(pk)
            context = {
                'invoice': invoice,
            }
            return render(request,'agency/invoice_detail.html',context)
        except Exception as exc:
            messages.warning(request,f'{exc}')
            return redirect('agency-home')
    
@login_required
def show_invoices(request):
    invoices = controller.invoices.get_invoices(request.user)
    context = {
        'invoices':invoices,
    }
    return render(request,'agency/invoices_list.html',context)

@login_required
def delete_booking(request,pk):
    is_deleted = controller.invoices.delete_invoice(pk)
    if is_deleted == True:
        messages.success(request,f'Deleted Booking and Invoice successfully!')
    else:
        messages.info(request,f'Booking does not exist!')
    return redirect('agency-home')
    
@login_required
def payment_choice(request,pk):
    if request.method == 'POST':
        payment_choice_form = forms.PaymentOptionForm(request.POST)
        if payment_choice_form.is_valid():
            payment_option = payment_choice_form.cleaned_data.get("payment_option")
            return redirect('agency-make-payment',pk,payment_option)
        else:
            messages.warning(request,f'Error, could not select payment option')
            return redirect('agency-payment-choice',pk)
    else:
        payment_choice_form = forms.PaymentOptionForm()
        context = {
            'payment_choice_form':payment_choice_form
        }
        return render(request,'agency/payment_choice.html',context)

@login_required
def make_payment(request,pk,payment_option):
    # invoice = controller.invoices.get_invoice(pk)
    if payment_option == 'CreditCard':
        if request.method == 'POST':
            payment_form = forms.PaymentbyCreditCardForm(request.POST)
            if payment_form.is_valid():
                amount = 0
                payment_date = payment_form.cleaned_data.get("payment_date")
                card_number = payment_form.cleaned_data.get("card_number")
                code = payment_form.cleaned_data.get("code")
                expiry_date = payment_form.cleaned_data.get("expiry_date")
                credit_card = controller.payments.create_credit_card(card_number,code,expiry_date)
                controller.make_payment(pk,amount,payment_date,credit_card)
                messages.success(request,f'Payment by Credit Card Successful!')
                return redirect('agency-invoices-list')
            else:    
                messages.warning(request,f'Error in validation!')
                return redirect('agency-make-payment',pk,payment_option) 
        else:
            payment_form = forms.PaymentbyCreditCardForm()
            context = {
                'payment_form':payment_form
            }
            return render(request,'agency/make_payment.html',context)   
    elif payment_option == 'Cash':
        if request.method == 'POST':
            payment_form = forms.PaymentbyCashForm(request.POST)
            if payment_form.is_valid():
                amount = payment_form.cleaned_data.get("amount")
                payment_date = payment_form.cleaned_data.get("payment_date")
                controller.make_payment(pk,amount,payment_date)
                messages.success(request,f'Payment by Cash Successful!')
                return redirect('agency-invoices-list')
            else:
                messages.warning(request,f'Error in validation!')
                return redirect('agency-make-payment',pk,payment_option)
        else:
            payment_form = forms.PaymentbyCashForm()
            context = {
                'payment_form':payment_form
            }
            return render(request,'agency/make_payment.html',context)  
            
    
        
    




# @login_required
# @user_passes_test(lambda u: u.is_superuser)
# def return_car(request,pk):
#     selected_rental = controller.rentals.get_rental(pk)
#     if request.method == 'POST':
#     return_form = forms.ReturnCarForm(request.POST)