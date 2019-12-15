from django.shortcuts import render,redirect
from django.views import View
from .forms import *
# Create your views here.
class VehicleDetailsView(View):
    form_class = VehicleDetailsForm
    template_name = 'vehicleapp/vehicledetails.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rodetails/')

        return render(request,self.template_name,{'form':form})

class VehicleModelView(View):
    form_class = VehicleModelForm
    template_name = 'vehicleapp/vehiclemodel.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vehiclemodel/')

        return render(request,self.template_name,{'form':form})
