from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from . models import *
from django.db.models import Q
import datetime
from django.utils import timezone
from django.contrib import messages
from . forms import *
import json


"""
    Display the homepage with available buses and fares.

    Retrieves all stops, buses, and fares from the database. Handles POST request
    to get source, destination, and travel date from the form submission. Retrieves
    relevant buses and calculates fares for the specified source and destination.
    Renders the 'buses.html' template with data and fares.

    Returns:
        HttpResponse: Rendered response containing the 'buses.html' template.
    """
def homepage(request):
    stops = Stop.objects.all()
    buses = Bus.objects.all()
    fares = {}
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']
        date_str = request.POST.get('traveldate', '')
        if date_str:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date = timezone.now().date()
        print(f'name:{source}')
        source_stop = Stop.objects.get(stop_name=source)
        destination_stop = Stop.objects.get(stop_name=destination)
        print(f'{source} {destination}')
        data = Bus.objects.filter(stops=source_stop).filter(stops=destination_stop ).filter(date_time=date).distinct()
        print(data)
        return render(request,'buses.html',{'data':data})
    return render(request,'index.html',{'stops':stops})

    """
    A function that handles user login. 
    It takes a request object as a parameter.
    If the request method is POST, it retrieves the email and password from the request, 
    validates the user credentials, and logs in the user if valid. 
    If the user is logged in successfully, it redirects to the home page.
    If the user credentials are invalid, it displays an error message and redirects to the login page.
    If the request method is not POST, it renders the login page.
    """
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(user_email = email, user_password = password)
        if user:
            request.session['user'] = user.user_name
            return redirect('/')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login')
    return render(request,'login.html')
    """
    Creates a new user account based on the provided request data.

    Parameters:
        request (HttpRequest): The HTTP request object containing the data for the new user account.

    Returns:
        HttpResponseRedirect: A redirect to the login page if the request method is POST and the user account is successfully created. Otherwise, returns an HttpResponse object containing the login page.
    """
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User(user_name = name, user_email = email, user_password = password)
        user_obj.save()
        return redirect('/login/')
    return render(request,'login.html')
    """
    A function to log out a user by removing 'user' from the session and redirecting to the homepage.
    """
def logout(request):
    del request.session['user']
    return redirect('/')
    """
    Render the 'account.html' template and return the rendered HTML as an HTTP response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """

def user_account(request):
    return render(request,'account.html')
    """
    Render the 'booking.html' template and return the rendered HTML as an HTTP response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
def booking(request):
    print("First")
    if request.method == 'POST':
        print("Second")
        selected_seats_json = request.POST.get('selected_seats', '[]')
        selected_seats = json.loads(selected_seats_json)
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            cleaned_data = form.cleaned_data
            source_stop = request.POST.get('source')
            destination_stop = request.POST.get('destination')
            # Iterate over the selected seats
            for seat_number in selected_seats:
                # Create a new Booking instance for each selected seat
                booking = Booking(
                    user=request.user,
                    bus=form.cleaned_data['bus'],
                    seat=Seat.objects.get(seat_id=seat_number),
                    passenger_name=cleaned_data['passenger_name'],
                    passenger_age=cleaned_data['passenger_age'],
                    booking_time=timezone.now(),
                    source_stop=source_stop,
                    destination_stop=destination_stop
                )
                # Save the booking to the database
                booking.save()
            # Redirect to the booking page
                return redirect('account')
    else:
        form = BookingForm()
    return render(request,'booking.html',{'form':BookingForm})