from django.contrib import admin
from inventoryapp.models import *
# Register your models here.
class Product_MasterAdmin(admin.ModelAdmin):
    list_display =['prod_code','prod_name','prod_tag','prod_tax']
admin.site.register(ProductMaster,Product_MasterAdmin)
admin.site.register(ProductInventory)
admin.site.register(VendorDetails)
