from django.test import TestCase
from django.urls import reverse

from .models import Invoice


class InvoiceDetailTests(TestCase):
    def test_invoice_detail_displays_requested_invoice(self):
        invoice = Invoice.objects.create(
            customer_name="Test Customer",
            invoice_number="INV-TEST",
            amount="125.00",
        )

        response = self.client.get(reverse("invoice_detail", args=[invoice.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, invoice.invoice_number)
        self.assertContains(response, invoice.customer_name)

    def test_invoice_detail_returns_404_for_missing_invoice(self):
        response = self.client.get(reverse("invoice_detail", args=[999]))

        self.assertEqual(response.status_code, 404)
