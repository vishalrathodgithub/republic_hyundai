from django.shortcuts import render,redirect
from django.views import View
from .forms import *
# Create your views here.
class ProductMasterView(View):
    form_class = ProductMasterForm
    template_name = 'inventoryapp/productmaster.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productmaster/')

        return render(request,self.template_name,{'form':form})


class VendorDetailsView(View):
    form_class = VendorDetailsForm
    template_name = 'inventoryapp/vendordetails.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vendordetails/')

        return render(request,self.template_name,{'form':form})


class ProductInventoryView(View):
    form_class = ProductInventoryForm
    template_name = 'inventoryapp/productinventory.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productinventory/')

        return render(request,self.template_name,{'form':form})
