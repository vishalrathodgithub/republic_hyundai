from django.forms import ModelForm
from taxapp.models import *
from django import forms

class TaxMasterForm(ModelForm):

    class Meta:
        labels={
         'tax_product_category':'Tax Product Category',
         'tax_hsn':'HSN',
         'tax_sgst':'SGST',
         'tax_cgst':'CGST',
         'tax_igst':'IGST',

         }
        model = TaxMaster
        fields = '__all__'


class FinancialYearForm(ModelForm):

    class Meta:
        labels = {
        'fin_year':'Financial Year',
        'fin_date_from':'From Date',
        'fin_date_to': 'Upto Date',
        }

        model = FinancialYear
        fields = '__all__'
        widgets = {
        'fin_date_from':forms.DateInput(attrs={'type':'date'}),
        'fin_date_to':forms.DateInput(attrs={'type':'date'}),
        }
