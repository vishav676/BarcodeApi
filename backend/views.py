# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import TicketListTable
from backend.serializers import TicketListSerializer


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
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTicketList(request, pk):
    ticketsList = TicketListTable.objects.get(id=pk)
    serializer = TicketListSerializer(instance=ticketsList, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
