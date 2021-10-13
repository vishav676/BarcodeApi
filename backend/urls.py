from django.urls import path

from django.contrib import admin
from . import views

urlpatterns = [

    # to get
    path('get/ticketLists', views.ticketList, name="getTicketsList"),
    path('get/tickets', views.getTickets, name="getTickets"),
    path('get/checkings', views.getCheckings, name="getCheckings"),
    path('get/histories', views.getScannings, name="getScannings"),
    path('get/checkingTicketRelations', views.getCheckingTicketList, name="ticketCheckingRelation"),


    # to create
    path('create/ticketList', views.createTicketList, name="createTicketList"),
    path('create/ticket', views.createTicket, name="createTicket"),
    path('create/history', views.createScanning, name="createScanning"),
    path('create/checking', views.createChecking, name="createChecking"),
    path('create/checkingTicketRelation', views.createCheckingTicketList, name="createCheckingTicket"),


    # to get one
    path('get/ticketList/<str:pk>', views.ticketOneList, name="getOneTicketList"),

    # to update
    path('update/ticketList/<str:pk>', views.updateTicketList, name="updateTicketList"),
    path('update/ticket/<str:pk>', views.updateTicket, name="updateTicket"),
    path('update/history/<str:pk>', views.updateTicket, name="updateTicket"),
    path('update/checking/<str:pk>', views.updateTicket, name="updateTicket"),
    path('update/checkingTicketRealtion/<str:pk>', views.updateTicket, name="updateTicket"),

]
