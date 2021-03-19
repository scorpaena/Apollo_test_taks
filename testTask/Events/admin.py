from django.contrib import admin
from .models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'info', 'timestamp', 'created_at' )
    list_filter = ('event_type', 'timestamp')

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
