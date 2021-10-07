from rest_framework import serializers
from .models import TicketListTable


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketListTable
        fields = '__all__'
