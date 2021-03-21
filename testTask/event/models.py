from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

class EventType(models.Model):
    name = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return self.name


def get_default_eventtype():
    obj, created = EventType.objects.get_or_create(id=1)
    return obj.id

def get_default_user():
    obj, created = User.objects.get_or_create(id=1)
    return obj.id


class Event(models.Model):
    user = models.ForeignKey(User, default=get_default_user, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, default=get_default_eventtype, on_delete=models.CASCADE)
    info = JSONField()
    timestamp = models.DateTimeField(default = timezone.now, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.event_type.name
