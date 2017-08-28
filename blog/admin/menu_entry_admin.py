from django.db import models
from django.utils.translation import ugettext as _
from django.contrib import admin
from web.entities import MenuEntry
from tandrini.support.actions import enable, disable


@admin.register(MenuEntry)
class MenuEntryAdmin:
    fields = (
        ('slug'),
        ('parent', 'position')
    )
    search_fields = ('slug',)
    list_display = ('__str__', 'enabled')
    actions = (enable, disable)
