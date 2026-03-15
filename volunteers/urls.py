from django.urls import path
from . import views

urlpatterns = [
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
]

