from django.db import models

# Create your models here.
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=45)
    state_initials = models.CharField(max_length=45)
    state_code = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'state'

    def __str__(self):
        return self.state_name


class District(models.Model):
    dist_id = models.AutoField(primary_key=True)
    dist_name = models.CharField(max_length=45)                   #d=District
    dist_state = models.ForeignKey(State, on_delete=models.CASCADE)  #d.dist_state.state_name

    class Meta:
        managed = True
        db_table = 'district'

    def __str__(self):
        return self.dist_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=45)
    city_dist = models.ForeignKey(District, on_delete=models.CASCADE)  #c.city_dist.dist_name

    class Meta:
        managed = True
        db_table = 'city'

    def __str__(self):
        return self.city_name


class CustomerType(models.Model):
    cust_type_id = models.AutoField(primary_key=True)
    cust_type_name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'customer_type'


    def __str__(self):
        return self.cust_type_name

class CustomerDetails(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=45)
    cust_dob = models.DateField(auto_now_add = False)
    cust_mob = models.CharField(max_length=13)
    cust_email = models.EmailField(blank=True, null=True)
    cust_addr = models.TextField(max_length=45)
    cust_city = models.ForeignKey(City, on_delete=models.CASCADE)
    cust_pin = models.CharField(max_length=6)
    cust_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    cust_created_date = models.DateTimeField(auto_now_add = True)



    class Meta:
        managed = True
        db_table = 'customer_details'

    def __str__(self):
        return self.cust_name
