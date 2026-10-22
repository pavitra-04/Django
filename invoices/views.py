from django.shortcuts import render
from django.http import HttpResponse
from .models import Invoice
from django.views.generic import ListView, DetailView,TemplateView
from django.shortcuts import render
from django.db.models import Count, Sum

#create a new record
from django.shortcuts import redirect

def create_invoice(request):
    Invoice.objects.create(
        customer_name='John Doe',
        invoice_number='INV-001',
        amount=1000.00,
        date_created='2026-10-20 10:00:00',
        is_paid=False,
        notes='Sample invoice'
    )

    return redirect('invoice_list')


#fetch
def show_one_invoice(request):
    invoice = Invoice.objects.get(id=5)
    data = {
        'invoice': invoice
    }
    return render(request, 'invoice_detail.html', {})

#filter
def show_unpaid_invoices(request):
    unpaid_invoices = Invoice.objects.filter(is_paid=False)
    return render(request, 'invoice_list.html', {
        'unpaid_invoices': unpaid_invoices
    })

#update
def mark_as_paid(request):
    Invoice.objects.filter(invoice_number='INV-001').update(is_paid=True)
    all_invoices = Invoice.objects.filter(is_paid=False)
    return render(request, 'invoice_list.html', {
        'all_invoices': all_invoices
    })
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
def home(request):
    invoices = Invoice.objects.all()

    customers = (
        Invoice.objects
        .values('customer_name')
        .annotate(
            invoice_count=Count('id'),
            total_billed=Sum('amount')
        )
        .order_by('customer_name')
    )

    context = {
        'total_invoices': invoices.count(),
        'paid_invoices': invoices.filter(is_paid=True).count(),
        'unpaid_invoices': invoices.filter(is_paid=False).count(),
        'total_amount': invoices.aggregate(
            total=Sum('amount')
        )['total'],
        'recent_invoices': invoices.order_by('-date_created')[:5],
        'customers': customers,
    }

    return render(request, 'home.html', context)

def invoice_list(request):
    all_invoices = Invoice.objects.all()
    unpaid_invoices = Invoice.objects.filter(is_paid=False)

    data = {
        'all_invoices': all_invoices,
        'unpaid_invoices': unpaid_invoices,
    }

    return render(request, 'invoice_list.html', data)
