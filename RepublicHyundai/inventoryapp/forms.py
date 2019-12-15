from django.forms import ModelForm
from inventoryapp.models import *
from django import forms

class ProductMasterForm(ModelForm):

    class Meta:
        labels = {
        'prod_code':'Product Code',
        'prod_name':'Product Name',
        'prod_tag':'Tag',
        'prod_tax':'Tax',

        }

        model = ProductMaster
        fields = '__all__'


class VendorDetailsForm(ModelForm):

    class Meta:
        labels = {
        'vendor_code':'Vendor Code',
        'vendor_comp_name':'Company Name',
        'vendor_name':'Vendor Name',
        'vendor_office_no':'Office Contact Number',
        'vendor_mobile_no':'Mobile Number.',
        'vendor_email_id':'Email-ID',
        'vendor_pan_no':'PAN Number',
        'vendor_gst_no':'GST Number',
        'vendor_address':'Office Address',
        'vendor_city':'City',
        'vendor_state':'State',
        'vendor_pin_code':'City PIN Code',


        }

        model = VendorDetails
        fields = '__all__'


class ProductInventoryForm(ModelForm):

    class Meta:
        labels = {
            'invent_prod' : 'Product Inventory',
            'prod_total_quantity' : 'Total Quantity',
            'prod_sold_quantity' : 'Sold Quantity',
            'prod_stock_remaining' : 'Remaining Stock',
            'prod_amount_without_tax' : 'Amount without Tax',
            'prod_current_selling_price' : 'Selling Price',
            'invent_vender' : 'Vendor',
            'prod_dispatch_date' : 'Dispatch Date',
            'prod_received_date' : 'Received Date',
            'prod_location' : 'Location',

        }
        model = ProductInventory
        fields = '__all__'
        widgets = {
        'prod_dispatch_date':forms.DateInput(attrs={'type':'date'}),
        'prod_recived_date':forms.DateInput(attrs={'type':'date'}),

        }
