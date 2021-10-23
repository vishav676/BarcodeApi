from rest_framework import serializers
from .models import TicketListTable, TicketTable, CheckingTable, ScanningTable, CheckingTicketListRelationship


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


class CheckingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CheckingTable
        fields = ["id", "checkingName", "checkingTime", "checkingDate"]


class ScanningTableSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ScanningTable
        fields = ["id", "scanningTime", "scanningCheckedMannualy",
                  "scanningIssue", "scanningNote", "scanningStatus",
                  "scanningTimesUsed", "scanningTicketNumber",
                  "scanningCheckingId"]


class CheckingTicketListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CheckingTicketListRelationship
        fields = ["id", "checkingListEventId", "checkingTicketListId"]
