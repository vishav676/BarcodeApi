# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import TicketListTable, TicketTable, CheckingTable, ScanningTable, CheckingTicketListRelationship
from backend.serializers import TicketListSerializer, TicketSerializer, CheckingSerializer, ScanningTableSerializer, \
    CheckingTicketListSerializer


@api_view(['GET'])
def ticketList(request):
    ticketsList = TicketListTable.objects.all()
    serializer = TicketListSerializer(ticketsList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ticketOneList(request, pk):
    ticketsList = TicketListTable.objects.get(id=pk)
    serializer = TicketListSerializer(ticketsList, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTicketList(request):
    serializer = TicketListSerializer(data=request.data)
    return saveToDb(serializer)


@api_view(['POST'])
def updateTicketList(request, pk):
    ticketsList = TicketListTable.objects.get(id=pk)
    serializer = TicketListSerializer(instance=ticketsList, data=request.data)
    return saveToDb(serializer)


@api_view(['POST'])
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    return saveToDb(serializer)


@api_view(['GET'])
def getTickets(request):
    allTickets = TicketTable.objects.all()
    serializer = TicketSerializer(allTickets, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTicket(request, pk):
    ticket = TicketTable.objects.get(id=pk)
    serializer = TicketSerializer(instance=ticket, data=request.data)
    return saveToDb(serializer)


@api_view(["GET"])
def getCheckings(request):
    allCheckings = CheckingTable.objects.all()
    serializer = CheckingSerializer(allCheckings, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createChecking(request):
    serializer = CheckingSerializer(data=request.data)
    return saveToDb(serializer)


@api_view(["PUT"])
def updateChecking(request, pk):
    checking = CheckingTable.objects.get(id=pk)
    serializer = CheckingSerializer(instance=checking, data=request.data)
    return saveToDb(serializer)


@api_view(["GET"])
def getScannings(request):
    allScannings = ScanningTable.objects.all()
    serializer = ScanningTableSerializer(allScannings, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createScanning(request):
    serializer = ScanningTableSerializer(data=request.data)
    return saveToDb(serializer)


@api_view(["PUT"])
def updateScanning(request, pk):
    scanning = ScanningTable.objects.get(id=pk)
    serializer = ScanningTableSerializer(instance=scanning, data=request.data)
    return saveToDb(serializer)


@api_view(["GET"])
def getCheckingTicketList(request):
    allRelation = CheckingTicketListRelationship.objects.all()
    serializer = CheckingTicketListSerializer(allRelation, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createCheckingTicketList(request):
    serializer = CheckingTicketListSerializer(data=request.data)
    return saveToDb(serializer)


@api_view(["PUT"])
def updateScanning(request, pk):
    relation = CheckingTicketListRelationship.objects.get(id=pk)
    serializer = CheckingTicketListSerializer(instance=relation, data=request.data)
    return saveToDb(serializer)


def saveToDb(serialized):
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)
