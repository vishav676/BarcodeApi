# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from backend.models import TicketListTable, CheckingTable, ScanningTable, TicketTable, CheckingTicketListRelationship

from django.contrib import admin

# Register your models here.
admin.site.register(TicketListTable)
admin.site.register(CheckingTable)
admin.site.register(ScanningTable)
admin.site.register(TicketTable)
admin.site.register(CheckingTicketListRelationship)

