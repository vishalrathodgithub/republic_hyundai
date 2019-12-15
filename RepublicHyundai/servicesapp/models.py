from django.db import models
from django.conf import settings
from taxapp.models import TaxMaster
from vehicleapp.models import VehicleDetails
from inventoryapp.models import ProductInventory,ProductMaster
from datetime import *
# Create your models here.

User = settings.AUTH_USER_MODEL


class LabourCategory(models.Model):
    lab_cat_id = models.AutoField(primary_key=True)
    lab_cat_name = models.CharField(max_length=30)


    class Meta:
        managed = True
        db_table = 'labour_category'

    def __str__(self):
        return self.lab_cat_name


class LabourDetails(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=45)
    lab_cat = models.ManyToManyField(LabourCategory)
    lab_mob_no = models.CharField(max_length=13)
    lab_addr = models.TextField()
    lab_city = models.CharField(max_length=30)
    lab_pin = models.IntegerField()


    class Meta:
        managed = True
        db_table = 'labour_details'

    def __str__(self):
        return self.lab_name

class RoWorktype(models.Model):
    ro_work_type_id = models.AutoField(primary_key=True)
    ro_work_type_name = models.CharField(max_length=45)
    rowork_lab = models.ManyToManyField(LabourDetails)

    class Meta:
        managed = True
        db_table = 'ro_worktype'

    def __str__(self):
        return self.ro_work_type_name

class LabourOperationMaster(models.Model):
    lab_op_id = models.AutoField(primary_key=True)
    lab_op_code = models.CharField(max_length=20)
    lab_op_name = models.CharField(max_length=45)
    labop_labcat = models.ManyToManyField(LabourCategory)
    lab_op_description = models.TextField()
    lab_op_work_hrs = models.FloatField(blank=True,null=True)
    lab_op_rate = models.FloatField(blank=True,null=True)
    lab_tax = models.ForeignKey(TaxMaster, on_delete=models.SET_NULL,null=True)
    lab_op_charges = models.FloatField(blank=True,null=True)



    class Meta:
        managed = True
        db_table = 'labour_operation_master'

    def __str__(self):
        return self.lab_op_name


class RoStatus(models.Model):
    ro_status_id = models.AutoField(primary_key=True)
    ro_status_name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'ro_status'

    def __str__(self):
        return self.ro_status_name




class RoDetails(models.Model):
    ro_id = models.AutoField(primary_key=True)
    ro_no = models.CharField(max_length=45)
    ro_invoice_no = models.CharField(max_length=20, blank=True, null=True)
    ro_service_type=models.CharField(max_length=20,default="Paid")
    rodetails_vehicle = models.OneToOneField(VehicleDetails, on_delete=models.CASCADE)
    ro_mileage = models.FloatField(blank=True, null=True)
    rodetails_worktype = models.ManyToManyField(RoWorktype)
    ro_created_by = models.CharField(max_length=20, blank=True, null=True)
    ro_received_date = models.DateField(auto_now_add=False)
    ro_received_time = models.TimeField(blank=True, null=True, default=time(0, 0))
    ro_open_date = models.DateField(auto_now_add=False)
    ro_open_time = models.TimeField(blank=True, null=True, default=time(0, 0))
    ro_promise_date = models.DateField(auto_now_add=False)
    ro_promise_time = models.TimeField(blank=True, null=True, default=time(0, 0))
    ro_closed_date = models.DateField(auto_now_add=False)
    ro_closed_time = models.TimeField(blank=True, null=True, default=time(0, 0))
    ro_closed_by = models.CharField(max_length=20, blank=True, null=True)
    ro_remarks = models.TextField()
    rodetails_rostatus = models.ForeignKey(RoStatus, on_delete = models.SET_NULL,null=True)


    class Meta:
        managed = True
        db_table = 'ro_details'


    def __str__(self):
        return self.rodetails_vehicle.veh_reg_no


class RoPartDetails(models.Model):
    ro_part_id = models.AutoField(primary_key=True)
    ropart_prod = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    ro_part_qty = models.IntegerField()
    ropart_rodetails = models.ManyToManyField(RoDetails)
    #tax_lab = models.FloatField()  #taken from taxapp.models.....>TaxMaster

    class Meta:
        managed = True
        db_table = 'ro_part_details'

    def __str__(self):
        return self.ropart_prod.prod_name
