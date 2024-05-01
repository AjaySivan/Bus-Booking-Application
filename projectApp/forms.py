from . models import *
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =['passenger_name','passenger_age','source_stop','destination_stop']
        labels = {
            'passenger_name':'Passenger Name',
            'passenger_age':'Passenger Age',
            'source_stop':'From',
            'destination_stop':'To',
        }
        widgets = {
            'passenger_name':forms.TextInput(attrs={'class': 'form-control'}),
            'passenger_age':forms.TextInput(attrs={'class':'form-control'}),
            'source_stop':forms.Select(attrs={'class':'form-control'}),
            'destination_stop':forms.Select(attrs={'class':'form-control'}),
        }