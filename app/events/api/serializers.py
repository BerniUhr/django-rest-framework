from rest_framework import serializers
from events.models import Category, Event

# JSON <--> Python Objekte


class EventInlineSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()   # Name des Authors auflösen (statt der id) bzw. die String Representation des Objekts

    class Meta:
        model = Event
        fields = ["id", "name", "author"]

class CategorySerializer(serializers.ModelSerializer):
    # events ist der related_name von dem Event Model
    events = EventInlineSerializer(many=True, read_only=True)   
    # many, weil 1:N Beziehung
    # read_only, weil Events in dieser View nur angezeigt werden sollen, nicht angelegt

    def to_representation(self, current_category_instance):
        """ Zusaetzliche Felder für Anzeige in View berechnen """
        representation =  super().to_representation(current_category_instance)
        representation["number_events"] = current_category_instance.events.count()
        return representation
    

    class Meta:
        model = Category
        fields = "__all__"