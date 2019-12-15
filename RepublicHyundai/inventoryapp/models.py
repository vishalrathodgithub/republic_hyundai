from django.db import models
from taxapp.models import TaxMaster
# Create your models here.


class ProductMaster(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_code = models.CharField(max_length=30)
    prod_name = models.CharField(max_length=30)
    prod_tag = models.CharField(max_length=30, blank=True, null=True)
    prod_tax = models.ForeignKey(TaxMaster, on_delete=models.SET_NULL,null=True)


    class Meta:
        managed = True
        db_table = 'product_master'

    def __str__(self):
        return self.prod_name

class VendorDetails(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_code = models.CharField(max_length=45)
    vendor_comp_name = models.CharField(max_length=45)
    vendor_name = models.CharField(max_length=45)
    vendor_office_no = models.CharField(max_length=13)
    vendor_mobile_no = models.CharField(max_length=13)
    vendor_email_id = models.EmailField(blank=True, null=True)
    vendor_pan_no = models.CharField(max_length=45,blank=True, null=True)
    vendor_gst_no = models.CharField(max_length=30,blank=True, null=True)
    vendor_address = models.CharField(max_length=45)
    vendor_city = models.CharField(max_length=20)
    vendor_state = models.CharField(max_length=45)
    vendor_pin_code = models.IntegerField()


    class Meta:
        managed = True
        db_table = 'vendor_details'


    def __str__(self):
        return self.vendor_comp_name


class ProductInventory(models.Model):
    prod_invent_id = models.AutoField(primary_key=True)
    invent_prod = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    prod_total_quantity = models.IntegerField()
    prod_sold_quantity = models.IntegerField(default=00)
    prod_stock_remaining = models.IntegerField()
    prod_amount_without_tax = models.FloatField()
    prod_current_selling_price = models.FloatField()
    invent_vender = models.ForeignKey(VendorDetails, on_delete=models.SET_NULL,null=True)
    prod_dispatch_date = models.DateField(auto_now_add=False)
    prod_received_date = models.DateField(auto_now_add=False)
    prod_location = models.CharField(max_length=45)


    class Meta:
        managed = True
        db_table = 'product_inventory'

    def __str__(self):
        return self.invent_prod.prod_name
