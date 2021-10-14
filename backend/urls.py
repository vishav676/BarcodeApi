from django.urls import path
from backend import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
