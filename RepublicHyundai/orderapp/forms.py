from django.forms import ModelForm
from orderapp.models import *
from django import forms

class OrderForm(ModelForm):

    class Meta:
        labels={
         'order_date':'Order Date',
         'order_vendor':'Order Vendor',
         'order_requested_by':'Requested By',
         'order_discount_percent':'Discount',
         'order_total_amount':'Total Amount',
         'order_status':'Status',
         'order_orderdetails':'Details',
         }

        model = Order
        fields = '__all__'
        widgets = {
        'order_date':forms.DateInput(attrs={'type':'date'}),
        }

class OrderDetailsForm(ModelForm):

    class Meta:
        labels={
        'order_prod':'Order Product Name',
        'order_product_quantity':'Product Quantity',
        'orderdetails_total_amount':'Total Amount',

        }

        model = OrderDetails
        fields = '__all__'
