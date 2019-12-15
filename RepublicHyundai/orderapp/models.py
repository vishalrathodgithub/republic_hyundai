from django.db import models
from inventoryapp.models import ProductMaster,ProductInventory,VendorDetails
# Create your models here.
class OrderDetails(models.Model):
    order_details_id = models.AutoField(primary_key=True)
    order_prod = models.ForeignKey(ProductMaster,on_delete=models.SET_NULL,null=True)
    order_product_quantity = models.IntegerField()
    orderdetails_total_amount = models.FloatField()
    # order_details_status = models.CharField(max_length=30)
    # order_invent = models.ManyToManyField(ProductInventory)


    class Meta:
        managed = True
        db_table = 'order_details'

    def __str__(self):
        return self.order_prod.prod_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=False)
    order_vendor = models.ForeignKey(VendorDetails,on_delete=models.SET_NULL,null=True)
    order_requested_by = models.CharField(max_length=30)
    order_discount_percent = models.FloatField(blank=True, null=True)
    order_total_amount = models.FloatField()
    order_status = models.CharField(max_length=30)
    order_orderdetails = models.ManyToManyField(OrderDetails)

    class Meta:
        managed = True
        db_table = 'order'

    def __str__(self):
        return str(self.order_date)
