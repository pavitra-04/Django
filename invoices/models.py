from django.db import models

# Create your models here.
#invoice model
class Invoice(models.Model):
    customer_name=models.CharField(max_length=200) #this will be a col in the database table
    invoice_number=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    notes=models.TextField(blank=True)

    def __str__(self):
        return self.invoice_number