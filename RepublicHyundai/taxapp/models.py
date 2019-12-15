from django.db import models

# Create your models here.


class TaxMaster(models.Model):
    tax_master_id = models.AutoField(primary_key=True)
    tax_product_category = models.CharField(max_length=40)
    tax_hsn = models.CharField(max_length=10)
    #tax_prod_name = models.CharField(max_length=40)
    tax_sgst = models.FloatField()
    tax_cgst = models.FloatField()
    tax_igst = models.FloatField()


    def __str__(self):
        return self.tax_product_category

    class Meta:
        managed = True
        db_table = 'tax_master'




class FinancialYear(models.Model):
    fin_id = models.AutoField(primary_key=True)
    fin_year = models.CharField(max_length=20)
    fin_date_from = models.DateField(auto_now_add=False)
    fin_date_to = models.DateField(auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'financial_year'

    def __str__(self):
        return self.fin_year
