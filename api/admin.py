from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'user', 'info', 'timestamp', 'create_at']
    list_filter = ['event_type', 'timestamp']


admin.site.site_header = "Event management"
admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
admin.site.unregister(Group)
