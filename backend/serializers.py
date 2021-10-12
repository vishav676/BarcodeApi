from rest_framework import serializers
from .models import TicketListTable, TicketTable


class TicketListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketListTable
        fields = ['id', 'ticketListName', 'ticketListCreated', 'ticketListUpdates']


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketTable
        fields = ['id', 'ticketNumber', 'ticketCustomerName', 'ticketInfo',
                  'ticketWarningNote', 'ticketUseable', 'ticketWarning',
                  'ticketListId']
