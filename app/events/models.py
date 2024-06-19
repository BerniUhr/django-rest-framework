# python .\manage.py startapp events
# python .\manage.py makemigrations events
# python manage.py sqlmigrate events 0001       # entstehende SQL Befehle anzeigen
# python .\manage.py migrate events

# Tabula Rasa: Migrationsdateien löschen und Datenbanktabelle löschen

# python .\manage.py shell
# from events.models import Category 
# sport = Category(name="Sport")
# sport.save()
# anzahl = Category.objects.count()
# Category.objects.get(pk=1).name
# Category.objects.filter(name__iexact="Lennon")   # Case insensitive
# Category.objects.filter(name__startswith="k")
# Category.objects.filter(created_at__year__gte=2024)
# qs = Category.objects.all()       # QuerySet wird zusammengebaut
# qs = qs.filter(name__startswith="K")
# qs = qs.filter(description__icontains="AG")
# list(qs)  # Datenbankabfrage wird erst jetzt ausgeführt


from django.db import models
from django.db.models.functions import Lower
from core.mixins import DatetimeMixin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Category(DatetimeMixin):
    # updated_by = models.ForeignKey
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = [Lower("name")]     # "-name", wenn absteigend
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"


    def __str__(self):
        return self.name

class Event(DatetimeMixin):

    class GroupSize(models.IntegerChoices):
        BIG = 20
        SMALL = 10
        UNLIMITED = 0

    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    group_size = models.IntegerField(choices=GroupSize.choices)
    # Was ist zu tun, wenn der User gelöscht wird: 
    # - CASCADE=Alle Events des USers löschen
    # - PROTECT=User kann nicht gelöscht werden, so lange noch ein Event von ihm besteht
    # - SET_NULL=User wird rausgelöscht (Feld muss NULL=True haben)
    author = models.ForeignKey(UserModel, 
                               on_delete=models.CASCADE, 
                               related_name="events")   # Zugriff vom User aus möglich: user.events.all() ("Related Manager")
    category = models.ForeignKey(Category, 
                               on_delete=models.CASCADE, 
                               related_name="events")   # Zugriff vom User aus möglich: user.events.all() ("Related Manager")

