from django.contrib import admin
from .models import Invoice


# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'invoice_number', 'amount', 'date_created', 'is_paid')
    list_filter = ('is_paid', 'date_created')
    search_fields = ('customer_name', 'invoice_number')
    ordering = ('-date_created',)

admin.site.register(Invoice, InvoiceAdmin)