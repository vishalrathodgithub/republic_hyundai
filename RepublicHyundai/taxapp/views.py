from django.shortcuts import render,redirect
from django.views import View
from .forms import *
# Create your views here.
class TaxMasterView(View):
    form_class = TaxMasterForm
    template_name = 'taxapp/taxmaster.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/taxmaster/')

        return render(request,self.template_name,{'form':form})


class FinancialYearView(View):
    form_class = FinancialYearForm
    template_name = 'taxapp/financialyear.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/financialyear/')

        return render(request,self.template_name,{'form':form})
