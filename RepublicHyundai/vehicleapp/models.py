from django.db import models
from customerapp.models import CustomerDetails
# Create your models here.

class VehicleCategory(models.Model):
    veh_cat_id = models.AutoField(primary_key=True)
    veh_cat_type = models.CharField(max_length=30)


    class Meta:
        managed = True
        db_table = 'vehicle_category'

    def __str__(self):
        return self.veh_cat_type



class VehicleModel(models.Model):
    veh_mod_id = models.AutoField(primary_key=True)
    veh_mod_name = models.CharField(max_length=30)
    veh_cat = models.ManyToManyField(VehicleCategory)
    class Meta:
        managed = True
        db_table = 'vehicle_model'

    def __str__(self):
        return self.veh_mod_name




class VehicleDetails(models.Model):
    veh_id = models.AutoField(primary_key=True)
    veh_cust = models.ForeignKey(CustomerDetails,on_delete=models.CASCADE)
    veh_ident_no = models.CharField(max_length=20, blank=True, null=True)
    veh_reg_no = models.CharField(max_length=40)
    veh_reg_date = models.DateField(auto_now_add = False)
    veh_name = models.CharField(max_length=30)
    veh_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    veh_color = models.CharField(max_length=20)
    veh_km = models.IntegerField()
    veh_eng_no = models.CharField(max_length=30)
    veh_chassis_no = models.CharField(max_length=30)
    veh_dealer_name = models.CharField(max_length=30,blank=True, null=True)
    veh_ins_comp_name = models.CharField(max_length=20,blank=True, null=True)
    veh_ins_policy_no = models.CharField(max_length=20,blank=True, null=True)
    veh_ins_code = models.CharField(max_length=20,blank=True, null=True)
    veh_free_services_remaining=models.IntegerField(default=3)
    veh_remarks = models.TextField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'vehicle_details'


    def __str__(self):
        return self.veh_reg_no
