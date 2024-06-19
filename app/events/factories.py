import factory
import random
from user.factories import UserFactory
from . import models
from datetime import datetime, timedelta
from django.utils import timezone

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta():
        model = models.Category
        django_get_or_create = ('name',)    # wenn es den name bereits gibt, lege nicht neu an
    
    name = factory.Iterator(["sport","outdoor","Pferdesport"])
    description = factory.Faker("paragraph", nb_sentences=3)


class EventFactory(factory.django.DjangoModelFactory):
    """ Eine Fabrik zum Anlegen eines zufälligen Events. """
    class Meta():
        model = models.Event
        # django_get_or_create = ("user_name",)  # wenn es den User bereits gibt, lege nicht neu an

    name = factory.Faker("sentence")
    author = factory.SubFactory(UserFactory)
    group_size = factory.LazyAttribute(
        lambda _: random.choice(list(models.Event.GroupSize.values))
    )
    category = factory.SubFactory(CategoryFactory)
    date = factory.Faker("date_time_between", 
                         start_date = datetime.now(),
                         end_date = datetime.now() + timedelta(days=100),
                         tzinfo = timezone.get_current_timezone()
                         )


# python manage.py shell:
# from events.factories import EventFactory
# EventFactory()  # legt ein Objekt an
# EventFactory.create_batch(20) # legt 20 Objekte an