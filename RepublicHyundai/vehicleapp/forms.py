from django.forms import ModelForm
from vehicleapp.models import *
from django import forms

class VehicleDetailsForm(ModelForm):

    class Meta:
        labels = {
        'veh_cust' : 'Vehicle Customer',
        'veh_ident_no' : 'Vehicle Customer',
        'veh_reg_no' : 'Vehicle Customer',
        'veh_reg_date' : 'Vehicle Customer',

        'veh_name' : 'Vehicle Customer',
        'veh_it_no' : 'Vehicle Customer',
        'veh_reg_no' : 'Vehicle Customer',
        'veh_reg_date' : 'Vehicle Customer',

         }
        model = VehicleDetails
        fields = '__all__'
        widgets = {
        'veh_reg_date':forms.DateInput(attrs={'type':'date'}),
        }


class VehicleModelForm(ModelForm):

    class Meta:
        model = VehicleModel
        fields = '__all__'
