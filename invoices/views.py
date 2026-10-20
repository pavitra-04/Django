from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,TemplateView
from django.shortcuts import render


def show_invoice(request):
    data= {
    'all_invoices': [
        {'number':1,'customer':'Rahul','amount':1003000},
        {'number':2,'customer':'Ramesh','amount':453000},
        {'number':3,'customer':'Suresh','amount':302400},
    ]
    }
    return render(request,'cust_name.html',data)
   

# Create your views here.
