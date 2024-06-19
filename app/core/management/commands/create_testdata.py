from django.core.management.base import BaseCommand
from events.factories import EventFactory
from events.models import Event

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Event.objects.all().delete()
        print("Creating events...")
        EventFactory.create_batch(100)
        print("Events created")

