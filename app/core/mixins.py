
from django.db import models
from django.views.decorators.cache import cache_page

class DatetimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Beim Anlegen setzen
    updated_at = models.DateTimeField(auto_now=True)      # Beim Updaten setzen

    class Meta:
        abstract = True     # Lege keine Datenbank an

class CacheMixin:
    """
    Caching von klassenbasierten List und Retrieve Views bei gleichbleibenden Daten
    """
    cache_timeout = 3600              # Anzahl der Sekunden, wie lange die Daten gechached bleiben

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *a, **k):
        return cache_page(self.get_cache_timeout())(super().dispatch)(*a, **k)