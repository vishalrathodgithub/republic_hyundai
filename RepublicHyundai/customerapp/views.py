from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from vehicleapp.models import *
from servicesapp.models import *
# Create your views here.

class StateView(View):
    form_class = StateForm
    template_name = 'customerapp/state.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/state/')

        return render(request,self.template_name,{'form':form})


class DistrictView(View):
    form_class = DistrictForm
    template_name = 'customerapp/district.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/district/')

        return render(request,self.template_name,{'form':form})


class CityView(View):
    form_class = CityForm
    template_name = 'customerapp/city.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/city/')

        return render(request,self.template_name,{'form':form})


class CustomerDetailsView(View):
    form_class = CustomerDetailsForm
    template_name = 'customerapp/CustomerDetails.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vehicledetails/')

        return render(request,self.template_name,{'form':form})

class ExistingCustomer(View):
    def get(self,request):
        a = request.GET.get("search")
        if a:
            data = RoDetails.objects.filter(rodetails_vehicle__veh_reg_no__icontains=a)
            print(data)
            return render(request, "customerapp/existingcustomer.html",{"data":data})
        return render(request, "customerapp/existingcustomer.html")
