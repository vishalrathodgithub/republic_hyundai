from django.shortcuts import render,redirect
from django.views import View
from servicesapp.models import *
from vehicleapp.models import *
from inventoryapp.models import *
from servicesapp.forms import *
from datetime import date
from functools import wraps
# Create your views here.


def preinvoice(request):
    preinvoice2 = RoDetails.objects.all().last()
    total_list=[]
    for ropart in preinvoice2.ropartdetails_set.all():
        for part in ropart.ropart_prod.productinventory_set.all():
            total_amt = (ropart.ro_part_qty) * (part.prod_current_selling_price)
        total_list.append(total_amt)
    sub_total = sum(total_list)

    return render(request,'invoiceapp/preinvoice.html',{'i':preinvoice2,"total_list":total_list,"sub_total":sub_total})

def finalinvoice(request,ro_id):
    
    data = RoDetails.objects.get(ro_id=ro_id)

    total_amt = []
    gst_per = []
    final_gst = []
    for i in data.ropartdetails_set.all():
        qty = i.ro_part_qty
        for a in i.ropart_prod.productinventory_set.all():
            amt = a.prod_current_selling_price
            total = amt*qty
            total_amt.append(total)
    sub_total=sum(total_amt)

    for i in data.ropartdetails_set.all():
        gst=i.ropart_prod.prod_tax.tax_igst
        gst_per.append(gst)

    for amt, gst in zip(total_amt, gst_per):
        tem = (amt*gst)/100
        final_gst.append(tem)
    tem2=sum(final_gst)
    final_total=tem2+sub_total
    grand_total = final_total - (final_total*10/100)

    to=data.ro_received_date
    inv=str(to).replace('-','')
    # print(data.ro_id)
    RoDetails.objects.filter(ro_id=ro_id).update(ro_invoice_no=inv)
    return render(request,'invoiceapp/finalinvoice.html',{'gst_per':tem2,'i':data,'sub_total':sub_total,'fianal_toatl':final_total,'grand_total':grand_total})




def updateprod(request,pk=None):

    data = RoPartDetails.objects.get(ro_part_id=pk)
    form = RoPartDetailsForm(instance=data)

    return render(request, "invoiceapp/ropartdetails1.html",{"form":form,"data":data,})




def updateprodinfo(request,pk=None):

    qty = request.POST["ro_part_qty"]
    data = RoPartDetails.objects.get(ro_part_id=pk)
    data1 = RoPartDetails.objects.filter(ro_part_id=pk).update(ro_part_qty=qty)
    data2 = RoDetails.objects.get(ropartdetails__ro_part_id=pk)



    return redirect(f'/finalinvoice/{data2.ro_id}/')

def calci(func):
    def inner(req,pk):

        finalinvoice = RoDetails.objects.get(ro_id=pk)


        for ropart in finalinvoice.ropartdetails_set.all():

            for part in ropart.ropart_prod.productinventory_set.all():
                total_qty = part.prod_total_quantity
                used_qty = ropart.ro_part_qty

                sold_qty = part.prod_sold_quantity + used_qty
                part.prod_stock_remaining = total_qty-sold_qty
                part.prod_sold_quantity = sold_qty
                part.save()

        response = func(req,pk)

        return response


    return wraps(func)(inner)




def deleteprod(request,pk):
    data = RoPartDetails.objects.get(ro_part_id=pk)
    data2 = RoDetails.objects.get(ropartdetails__ro_part_id=pk)

    if request.method=="POST":
        data.delete()

    return redirect(f'/finalinvoice/{data2.ro_id}/')


@calci
def print(request,pk):
    data = RoDetails.objects.get(ro_id=pk)

    total_amt = []
    gst_per = []
    final_gst = []
    for i in data.ropartdetails_set.all():
        qty = i.ro_part_qty
        for a in i.ropart_prod.productinventory_set.all():
            amt = a.prod_current_selling_price
            total = amt*qty
            total_amt.append(total)
    sub_total=sum(total_amt)

    for i in data.ropartdetails_set.all():
        gst=i.ropart_prod.prod_tax.tax_igst
        gst_per.append(gst)

    for amt, gst in zip(total_amt, gst_per):
        tem = (amt*gst)/100
        final_gst.append(tem)
    tem2=sum(final_gst)
    final_total=tem2+sub_total
    grand_total = final_total - (final_total*10/100)

    to=data.ro_received_date
    inv=str(to).replace('-','')
    # print(data.ro_id)
    RoDetails.objects.filter(ro_id=pk).update(ro_invoice_no=inv)
    return render(request,'invoiceapp/print.html',{'gst_per':tem2,'i':data,'sub_total':sub_total,'fianal_toatl':final_total,'grand_total':grand_total})

def addnewprod(request,pk):
    finalinvoice = RoDetails.objects.get(ro_id=pk)
    form = RoPartDetailsForm()
    if request.method =="POST":
        form = RoPartDetailsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/finalinvoice/{finalinvoice.ro_id}/')
    return render(request,"invoiceapp/addnewprod.html",{"form":form,"finalinvoice":finalinvoice})

def printpreinvoice(request):
    preinvoice2 = RoDetails.objects.all().last()
    total_list=[]
    for ropart in preinvoice2.ropartdetails_set.all():
        for part in ropart.ropart_prod.productinventory_set.all():
            total_amt = (ropart.ro_part_qty) * (part.prod_current_selling_price)
        total_list.append(total_amt)
    sub_total = sum(total_list)

    return render(request,'invoiceapp/printpreinvoice.html',{'i':preinvoice2,"total_list":total_list,"sub_total":sub_total})
