from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,TemplateView
from django.shortcuts import render


def show_invoice(request):
    data= {
        'customer_name': "Sona",
        'invoice_total': 150000
    }
    return render(request,'cust_name.html',data)
   

# Create your views here.
