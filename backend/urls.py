from django.urls import path

from django.contrib import admin
from . import views
urlpatterns = [
    path('tickets-List', views.ticketList, name="tickets-list"),
    path('ticket-List/<str:pk>', views.ticketOneList, name="ticket-list"),
    path('ticketList-create', views.createTicketList, name="create-tickets-list"),
    path('ticketList-updatation/<str:pk>', views.updateTicketList, name="update-tickets-list"),
]
