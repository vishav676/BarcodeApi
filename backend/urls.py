from django.urls import path
from backend import views

# URL patterns to access the specific endpoint when deployed.
urlpatterns = [

    path('ticketLists/', views.TicketList.as_view()),
    path('ticketLists/<str:pk>', views.TicketListDetail.as_view()),

    path('ticket/', views.Ticket.as_view()),
    path('ticket/<str:pk>', views.TicketDetail.as_view()),

    path('scanning/', views.Scanning.as_view()),
    path('scanning/<str:pk>', views.ScanningDetail.as_view()),

    path('checking/', views.Checking.as_view()),
    path('checking/<str:pk>', views.CheckingDetail.as_view()),

    path('checkingTicket/', views.CheckingTicketRelation.as_view()),
    path('checkingTicket/<str:pk>', views.CheckingTableRelationDetail.as_view()),

]
