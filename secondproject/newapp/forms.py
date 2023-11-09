from django import forms
from .models import Booking
from django_countries import countries

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'country': forms.Select(choices=countries),
        }
