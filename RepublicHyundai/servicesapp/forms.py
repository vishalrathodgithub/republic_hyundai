from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets as wid
from servicesapp.models import *


class LabourDetailsForm(ModelForm):

    class Meta:
        labels={
         'lab_name':'Labour Name',
         'lab_cat':'Labour Category',
         'lab_mob_no':'Mobile Number',
         'lab_addr':'Address',
         'lab_city':'City',
         'lab_pin':'PIN Code',

         }
        model = LabourDetails
        fields = '__all__'


class LabourOperationMasterForm(ModelForm):

    class Meta:
        labels={
         'lab_op_code':'Labour Operation Code',
         'lab_op_name':'Labour Name ',
         'labop_labcat':'Category',
         'lab_op_description':'Labour Operation Description',
         'lab_op_work_hrs':'Hours',
         'lab_op_rate':'Rate Per Hour',
         'lab_tax':'Tax',
         'lab_op_charges':'Charges',

         }
        model = LabourOperationMaster
        fields = '__all__'

class RoDetailsForm(ModelForm):

    class Meta:
        labels={
         'ro_no':'RO Number',
         'ro_service_type':'Service Type',
         'rodetails_vehicle':'Vehicle Details',
         'ro_mileage':'Mileage',
         'rodetails_worktype':'Work Type',
         'ro_created_by':'Created By',
         'ro_received_date':'Received Date',
         'ro_received_time':'Received Time',
         'ro_open_date':'Open Date',
         'ro_open_time':'Open Time',
         'ro_promise_date':'Promise Date',
         'ro_promise_time':'Promise Time',
         'ro_closed_date':'Closed Date',
         'ro_closed_time':'Closed Time',
         'ro_closed_by':'Closed By',
         'ro_remarks':'Remarks',
         'rodetails_rostatus':'Status',


         }
        model = RoDetails
        # fields = '__all__'
        exclude = ["ro_invoice_no"]
        widgets = {
        "ro_received_date":forms.DateInput(attrs={'type':'date'}),
        "ro_received_time":forms.TimeInput(attrs={'type':'time'}),
        "ro_open_date":forms.DateInput(attrs={'type':'date'}),
        "ro_open_time":forms.TimeInput(attrs={'type':'time'}),
        "ro_closed_date":forms.DateInput(attrs={'type':'date'}),
        "ro_closed_time":forms.TimeInput(attrs={'type':'time'}),
        "ro_promise_date":forms.DateInput(attrs={'type':'date'}),
        "ro_promise_time":forms.TimeInput(attrs={'type':'time'}),
        }

class RoPartDetailsForm(ModelForm):

    class Meta:
        labels={
        'ropart_prod':'RO Product Part',
        'ro_part_qty':'Quantity',
        'ropart_rodetails':'Part Details',
        }
        model = RoPartDetails
        fields = '__all__'
