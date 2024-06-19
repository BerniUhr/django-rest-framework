from rest_framework import generics, permissions, authentication
from django.contrib.auth import get_user_model      # Holt sich das in settings.py eingestellte User Model
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
# import logging

# logger = logging.logger("django")

class ListUserView(generics.ListAPIView):
    """ View zum Auflisten von Usern 
    api/users/
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all() # objects= manager


class CreateUserView(generics.CreateAPIView):
    """ View zum Anlegen von Usern 
    api/users/create
    """
    serializer_class = UserSerializer
    permission_classes = []     # Jeder darf einen User anlegen
    
class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Aktuellen User holen und ändern
    api/users/about   # curl -X PATCH -d "user_name=Uhr" http://127.0.0.1:8000/api/users/about -H "Authorization: Token 0e51be3480c7a44ba30ea9079b1e21b43b057105"
    """
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication] # Welche Authentifizierungsmoeglichkeiten sind erlaubt?
    permission_classes = [permissions.IsAuthenticated]              # Wer darf das?

    def get_object(self):
        # Holt den aktuell eingeloggten User
        return self.request.user


class EmailconfirmationUserView(View):
    def get(self, request, uid, confirm_token):      # siehe urls.py
        try:
            user = get_user_model().objects.get(pk=uid)
        except Exception as e:
            user = None
            print("User wurde nicht erkannt")
            # logger.error("User wurde nicht erkannt")

        if user and user.email_confirmed == True:
            return HttpResponse("Email wurde bereits bestätigt")

        if user and str(user.email_token) == confirm_token:
            user.email_confirmed = True
            # TODO: Email an System Admin schicken und um Aktivierung bitten
            user.save()
            return HttpResponse("Email wurde erfolgreich bestätigt")
        return HttpResponse("Email wurde Bestätigung war NICHT erfolgreich")

