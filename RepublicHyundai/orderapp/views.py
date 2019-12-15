from django.shortcuts import render,redirect
from django.views import View
from .forms import *
# Create your views here.
class OrderView(View):
    form_class = OrderForm
    template_name = 'orderapp/order.html'

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order/')

        return render(request,self.template_name,{'form':form})


class OrderDetailsView(View):
    form_class = OrderDetailsForm
    template_name = 'orderapp/orderdetails.html'

    def get(self,request):
        form = self.form_class()
        ord_det = OrderDetails.objects.all()
        return render(request,self.template_name,{'form':form,"ord_det":ord_det})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orderdetails/')

        return render(request,self.template_name,{'form':form})
