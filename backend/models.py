# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# Database model file.

class TicketListTable(models.Model):  # Create the table with name TicketListTable
    ticketListName = models.CharField(max_length=50)  # table column to save the strings.
    ticketListCreated = models.DateTimeField()  # table column to save when item was inserted in the database.
    ticketListUpdates = models.DateTimeField() # table column to save when the table was recently updated.

    def __str__(self):
        return self.ticketListName

    class Meta:
        app_label = "backend"
        db_table = "TicketListTable"


class TicketTable(models.Model):
    ticketNumber = models.CharField(max_length=50)
    ticketCustomerName = models.CharField(max_length=50)
    ticketInfo = models.CharField(max_length=100, blank=True)
    ticketWarningNote = models.CharField(max_length=100, blank=True)
    ticketUseable = models.IntegerField()
    ticketWarning = models.CharField(max_length=50, blank=True)
    ticketListId = models.ForeignKey(TicketListTable, on_delete=models.CASCADE, related_name="listTable_tickets")

    def __str__(self):
        return self.ticketNumber

    class Meta:
        app_label = "backend"
        db_table = "TicketTable"


class CheckingTable(models.Model):
    checkingName = models.CharField(max_length=50)
    checkingTime = models.DateTimeField()
    checkingDate = models.DateField()

    def __str__(self):
        return self.checkingName

    class Meta:
        app_label = "backend"
        db_table = "CheckingTable"


class ScanningTable(models.Model):
    scanningStatus = models.CharField(max_length=50)
    scanningTime = models.DateTimeField()
    scanningCheckedMannualy = models.BooleanField()
    scanningIssue = models.CharField(max_length=100, blank=True)
    scanningNote = models.CharField(max_length=100, blank=True)
    scanningTimesUsed = models.IntegerField()
    scanningTicketNumber = models.CharField(max_length=50)
    scanningCheckingId = models.ForeignKey(CheckingTable, on_delete=models.CASCADE, related_name="event_history")

    def __str__(self):
        return self.scanningTicketNumber

    class Meta:
        app_label = "backend"
        db_table = "ScanningTable"


class CheckingTicketListRelationship(models.Model):
    checkingListEventId = models.ForeignKey(CheckingTable, on_delete=models.CASCADE, related_name="event_relation")
    checkingTicketListId = models.ForeignKey(TicketListTable, on_delete=models.CASCADE, related_name="list_relation")

    class Meta:
        app_label = "backend"
        db_table = "CheckingTicketListRelationship"
