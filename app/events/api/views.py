from rest_framework import generics
from .serializers import CategorySerializer
from events.models import Category, Event

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.services import call_external_api, ServiceException
from core.mixins import CacheMixin

EXTERNAL_API_URL = "https://friendlybytes.net/api/blog/category/"

class ExternalApiView(APIView):
    """
    api/events/external?query=khgjkg
    """
    def get(self, request):
        # request.query_params
        try:
            query = request.query_params['query']
            response = call_external_api(url=EXTERNAL_API_URL, query=query)
        except KeyError:
            response = {"error": "Parameter query muss angegeben werden"}
            return Response( data=response, status=status.HTTP_400_BAD_REQUEST )    
        except ServiceException as e:
            response = {"error": str(e)}
            return Response( data=response, status=status.HTTP_400_BAD_REQUEST )    
        return Response( data=response, status=status.HTTP_200_OK )


class CategoryListCreateView(CacheMixin, generics.ListCreateAPIView):
    """ View zum Auflisten und Anlegen von Category.
    # CacheMixin nur verwenden, wenn Daten tendentiell statisch gleichbleibend
    /api/events/categories
    """
    serializer_class = CategorySerializer
    # Verweise auf andere Models vorladen. Damit werden wesentlich weniger SQL abfragen benötigt --> schneller
    queryset = Category.objects.prefetch_related("events", "events__author") # objects= manager

    permission_classes = []


