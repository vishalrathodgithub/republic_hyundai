from django.shortcuts import render
from .forms import *
from .models import *
from servicesapp.models import *

# Create your views here.
def historyview(request):
    rc = RcHistory()
    rodetail = RoDetails.objects.all().last()
    total_list=[]
    gst_list = []
    final_gst = []

    for ropart in rodetail.ropartdetails_set.all():
        rc.prod_qty = ropart.ro_part_qty

        for part in ropart.ropart_prod.productinventory_set.all():

            total_amt = (ropart.ro_part_qty) * (part.prod_current_selling_price)
            total_list.append(total_amt)

            gst_per = part.invent_prod.prod_tax.tax_igst
            gst_list.append(gst_per)



    for amt,gstt in zip(total_list,gst_list):
        value = (amt*gstt)/100
        final_gst.append(value)

    sum_value=sum(final_gst)
    sub_total = sum(total_list)
    final_total = sum_value + sub_total



    return render(request, "historyapp/history.html")
