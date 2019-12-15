from django.contrib import admin
from taxapp.models import *
# Register your models here.
class TaxMasterAdmin(admin.ModelAdmin):
    list_display =['tax_product_category','tax_hsn','tax_sgst','tax_cgst','tax_igst']
admin.site.register(TaxMaster,TaxMasterAdmin)
admin.site.register(FinancialYear)
