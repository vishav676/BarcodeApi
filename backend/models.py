# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class TicketListTable(models.Model):
    ticketListId = models.AutoField(primary_key=True)
    ticketListName = models.CharField(max_length=50)
    ticketListCreated = models.DateTimeField()
    ticketListUpdates = models.DateTimeField()

    def __str__(self):
        return self.ticketListName

    class Meta:
        app_label = "backend"
        db_table = "TicketListTable"


class TicketTable(models.Model):
    ticketId = models.AutoField(primary_key=True)
    ticketNumber = models.CharField(max_length=50)
    ticketCustomerName = models.CharField(max_length=50)
    ticketInfo = models.CharField(max_length=100)
    ticketWarningNote = models.CharField(max_length=100)
    ticketUseable = models.IntegerField()
    ticketWarning = models.CharField(max_length=50)
    ticketListId = models.ForeignKey(TicketListTable, on_delete=models.CASCADE, related_name="listTable_tickets")

    def __str__(self):
        return self.ticketNumber

    class Meta:
        app_label = "backend"
        db_table = "TicketTable"


class CheckingTable(models.Model):
    checkingId = models.AutoField(primary_key=True)
    checkingName = models.CharField(max_length=50)
    checkingTime = models.DateTimeField()
    checkingDate = models.DateField()

    def __str__(self):
        return self.checkingName

    class Meta:
        app_label = "backend"
        db_table = "CheckingTable"


class ScanningTable(models.Model):
    scanningId = models.AutoField(primary_key=True)
    scanningStatus = models.CharField(max_length=50)
    scanningTime = models.DateTimeField()
    scanningCheckedMannualy = models.BooleanField()
    scanningIssue = models.CharField(max_length=100)
    scanningNote = models.CharField(max_length=100)
    scanningTimesUsed = models.IntegerField()
    scanningTicketNumber = models.CharField(max_length=50)
    scanningCheckingId = models.ForeignKey(CheckingTable, on_delete=models.CASCADE, related_name="event_history")

    def __str__(self):
        return self.scanningTicketNumber

    class Meta:
        app_label = "backend"
        db_table = "ScanningTable"


class CheckingTicketListRelationship(models.Model):
    primary_id = models.AutoField(primary_key=True)
    checkingListEventId = models.ForeignKey(CheckingTable, on_delete=models.CASCADE, related_name="event_relation")
    checkingTicketListId = models.ForeignKey(TicketListTable, on_delete=models.CASCADE, related_name="list_relation")

    def __str__(self):
        return self.primary_id

    class Meta:
        app_label = "backend"
        db_table = "CheckingTicketListRelationship"
