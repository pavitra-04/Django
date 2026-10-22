from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<int:pk>/', views.show_one_invoice, name='invoice_detail'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
]
