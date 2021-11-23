from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from backend.models import TicketListTable, TicketTable, CheckingTable, ScanningTable, CheckingTicketListRelationship
from backend.serializers import TicketListSerializer, TicketSerializer, CheckingSerializer, ScanningTableSerializer, \
    CheckingTicketListSerializer


# TicketList class to return data from database or to save data.
class TicketList(GenericAPIView):
    serializer_class = TicketListSerializer

    def get(self, request):
        ticketsList = TicketListTable.objects.all()
        serializer = TicketListSerializer(ticketsList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketListSerializer(data=request.data)
        return saveToDb(serializer)


# TicketList class to update data to database
class TicketListDetail(GenericAPIView):
    serializer_class = TicketListSerializer
    queryset = TicketListTable.objects

    def put(self, request, pk):
        ticketsList = TicketListTable.objects.get(id=pk)
        serializer = TicketListSerializer(instance=ticketsList, data=request.data)
        return saveToDb(serializer)


# Ticket class to return data from database or to save data.
class Ticket(GenericAPIView):
    serializer_class = TicketSerializer

    def get(self, request):
        allTickets = TicketTable.objects.all()
        serializer = TicketSerializer(allTickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        return saveToDb(serializer)


# Ticket class to update data to database
class TicketDetail(GenericAPIView):
    serializer_class = TicketSerializer
    queryset = TicketTable.objects

    def put(self, request, pk):
        ticket = TicketTable.objects.get(id=pk)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        return saveToDb(serializer)


# Scanning class to return data from database or to save data.
class Scanning(GenericAPIView):
    serializer_class = ScanningTableSerializer

    def get(self, request):
        allScannings = ScanningTable.objects.all()
        serializer = ScanningTableSerializer(allScannings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScanningTableSerializer(data=request.data)
        return saveToDb(serializer)


# Scanning class to update data to database
class ScanningDetail(GenericAPIView):
    serializer_class = ScanningTableSerializer
    queryset = ScanningTable.objects

    def put(self, request, pk):
        scanning = ScanningTable.objects.get(id=pk)
        serializer = ScanningTableSerializer(instance=scanning, data=request.data)
        return saveToDb(serializer)


# Checking class to return data from database or to save data.
class Checking(GenericAPIView):
    serializer_class = CheckingSerializer

    def get(self, request):
        allCheckings = CheckingTable.objects.all()
        serializer = CheckingSerializer(allCheckings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckingSerializer(data=request.data)
        return saveToDb(serializer)


# Checking class to update data to database
class CheckingDetail(GenericAPIView):
    serializer_class = CheckingSerializer
    queryset = CheckingTable.objects

    def put(self, request, pk):
        checking = CheckingTable.objects.get(pk)
        serializer = CheckingSerializer(instance=checking, data=request.data)
        return saveToDb(serializer)


# CheckingTicketRelation class to return data from database or to save data.
class CheckingTicketRelation(GenericAPIView):
    serializer_class = CheckingTicketListSerializer

    def get(self, request):
        allRelation = CheckingTicketListRelationship.objects.all()
        serializer = CheckingTicketListSerializer(allRelation, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckingTicketListSerializer(data=request.data)
        return saveToDb(serializer)


# CheckingTableRelationDetail class to update data to database
class CheckingTableRelationDetail(GenericAPIView):
    serializer_class = CheckingTicketListSerializer
    queryset = CheckingTicketListRelationship.objects

    def put(self, request, pk):
        relation = CheckingTicketListRelationship.objects.get(id=pk)
        serializer = CheckingTicketListSerializer(instance=relation, data=request.data)
        return saveToDb(serializer)


# Save the data to db.
def saveToDb(serialized):
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)
