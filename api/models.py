from django.db import models


class EventType(models.Model):
    name = models.CharField("Event name", max_length=120)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.CharField("User", max_length=120, primary_key=True)
    event_type = models.ForeignKey(EventType, related_name="events", on_delete=models.CASCADE, verbose_name="Event Type")
    info = models.JSONField("JSON Info")
    timestamp = models.DateTimeField("Time stamp")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
