from rest_framework import serializers
from .models import TicketListTable


class TicketListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = TicketListTable
        fields = ['id','ticketListName','ticketListCreated','ticketListUpdates']