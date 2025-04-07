#from django.test import TestCase

# Create your tests here.

# tdapp/tests.py

import pytest
from django.urls import resolve
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from tdapp.models import Booking
from tdapp.views import login_view, signup, logout_view

# ✅ Enable DB access for these tests
@pytest.mark.django_db
def test_booking_model_valid():
    user = User.objects.create(username="testuser")
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)

    booking = Booking.objects.create(
        user=user,
        name="Alice",
        email="alice@example.com",
        phone="1234567890",
        check_in=today,
        check_out=tomorrow,
        guests=2
    )

    assert str(booking) == f"Booking for Alice ({today} - {tomorrow})"

@pytest.mark.django_db
def test_booking_model_invalid_guests():
    user = User.objects.create(username="testuser2")
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)

    booking = Booking(
        user=user,
        name="Bob",
        email="bob@example.com",
        phone="9876543210",
        check_in=today,
        check_out=tomorrow,
        guests=0
    )

    with pytest.raises(Exception):
        booking.full_clean()

# ✅ URL tests
def test_login_url_resolves():
    resolver = resolve('/login/')
    assert resolver.func == login_view

def test_signup_url_resolves():
    resolver = resolve('/signup/')
    assert resolver.func == signup

def test_logout_url_resolves():
    resolver = resolve('/logout/')
    assert resolver.func == logout_view
