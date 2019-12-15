from django.db import models

# Create your models here.
class RcHistory(models.Model):
    rc_hist_id = models.AutoField(primary_key=True)
    ro_invoice_no = models.CharField(max_length=30)
    veh_reg_no = models.CharField(max_length=15)
    veh_name = models.CharField(max_length=20)
    veh_model = models.CharField(max_length=15)
    veh_km = models.PositiveIntegerField()
    cust_name = models.CharField(max_length=30)
    cust_mob = models.CharField(max_length=15)
    cust_email = models.EmailField(null=True , blank=True)
    cust_addr = models.TextField()
    veh_received_date = models.DateField(auto_now_add=False)
    ro_open_date = models.DateField(auto_now_add=False)
    ro_closed_date = models.DateField(auto_now_add=False)
    prod_name = models.CharField(max_length=30)
    prod_qty = models.PositiveIntegerField()
    ro_lab = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = "rc_history"

    def __str__(self):
        return self.veh_reg_no
