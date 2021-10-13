from django.urls import path

from django.contrib import admin
from . import views

urlpatterns = [

    # to get
    path('get/allTicketsList', views.ticketList, name="getTicketsList"),
    path('get/allTickets', views.getTickets, name="getTickets"),

    # to create
    path('create/ticketList', views.createTicketList, name="createTicketList"),
    path('create/ticket', views.createTicket, name="createTicket"),

    # to get one
    path('get/ticketList/<str:pk>', views.ticketOneList, name="getOneTicketList"),

    # to update
    path('update/ticketList/<str:pk>', views.updateTicketList, name="updateTicketList"),
    path('update/ticket/<str:pk>', views.updateTicket, name="updateTicket"),

]
