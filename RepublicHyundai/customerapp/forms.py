from django.forms import ModelForm
from customerapp.models import *
from django import forms

class StateForm(ModelForm):

    class Meta:
        labels = {
        'state_name':'State Name',
        'state_initials':'State Initial',
        'state_code' : 'State Code',

        }
        model = State
        fields = '__all__'


class DistrictForm(ModelForm):

    class Meta:
        labels = {
        'dist_name':'District Name',
        'dist_state':'State Name',

        }
        model = District
        fields = '__all__'


class CityForm(ModelForm):

    class Meta:
        labels = {
        'city_name':'City Name',
        'city_dist':'District Name',

        }
        model = City
        fields = '__all__'



class CustomerDetailsForm(ModelForm):

    class Meta:
        labels = {
        'cust_name':'Customer Name',
        'cust_email':'Email-ID',
        'cust_mob':'Mobile Number',
        'cust_addr':'Address',
        'cust_city':'City',
        'cust_pin':'City PIN Code',
        'cust_type':'Customer Type',
        }
        model = CustomerDetails
        fields = '__all__'
        widgets = {
        'cust_dob':forms.DateInput(attrs={'type':'date'}),
        }
