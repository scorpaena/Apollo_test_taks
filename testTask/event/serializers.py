from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User
from .models import Event, EventType


class EventSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    event_type = serializers.CharField(max_length = 100)

    class Meta:
        model = Event
        fields = [
            'id',
            'user',
            'event_type',
            'info',
            'timestamp',
            'created_at'
        ]
        read_only_fields = ['created_at']
        depth = 0

    def create(self, validated_data):
        event, _ = EventType.objects.get_or_create(name=validated_data['event_type'])
        validated_data['event_type'] = event
        return Event.objects.create(**validated_data)


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = [
            'id',
            'name',
        ]
