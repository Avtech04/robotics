from django.contrib import admin
from .models import Event, Participant

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'slug', 'time_of_creation')
    search_fields = ('event_name', 'slug')
    filter_horizontal = ('participants',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
