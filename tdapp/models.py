from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone 
from django.contrib.auth.models import User  

# Create your models here.

def validate_date(value):
    if value < timezone.now().date():
        raise ValidationError("Booking date cannot be in the past.")

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)  # Link booking to a user
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateField(validators=[validate_date])
    check_out = models.DateField(validators=[validate_date])
    guests = models.PositiveIntegerField()


    def clean(self):
        """Custom validation for check-in and check-out dates."""
        if self.check_out <= self.check_in:
            raise ValidationError("Check-out date must be after check-in date.")
        
        if self.guests < 1:
            raise ValidationError("At least one guest must be selected.")

    def __str__(self):
        return f"Booking for {self.name} ({self.check_in} - {self.check_out})"

