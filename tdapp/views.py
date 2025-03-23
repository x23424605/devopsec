from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from django.urls import reverse





# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password")
    # GET requests, just render the login page
    return render(request, 'td/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect("login")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")  # Redirect to login page after successful registration

    return render(request, "td/signup.html")

# def register(request):
#     return render(request, 'td/signup.html')

def dashboard(request):
    return render(request, 'td/dashboard.html')

# def travel(request):
#     return render(request, "td/travel.html")

def room_booking(request, country):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect(reverse('success', kwargs={'booking_id': booking.id})) # passing booking id to success page
    else:
        form = BookingForm()

    return render(request, "td/booking.html", {"form": form, "country": country})
    
def success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.user = request.user  # Associate the booking with the logged-in user
    booking.status = "Confirmed"
    booking.save()
    return render(request, 'confirmation.html', {'booking': booking})

def myplans(request):
    bookings = Booking.objects.filter(user=request.user, status="Confirmed")
    return render(request, 'myplans.html', {'bookings': bookings})