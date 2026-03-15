from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate_view, name='donate'),
    path('verify/', views.verify_payment, name='verify_payment'),
    path('success/<int:pk>/', views.donation_success, name='donation_success'),
]

