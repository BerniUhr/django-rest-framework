from django.db import models
import uuid
from django.core.mail import send_mail

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager): # Schnittstelle zur Datenbank
    """" Custom user manager für das CustomUser Model """

    def send_confirmation_mail(self, user):
        """ Sende Bestätigungsmail an den User senden """
        url = f"http://127.0.0.1/api/users/confirm/{user.pk}/{user.email_token}"
        send_mail(
            subject="Bestätigung Ihrer Email",
            message=f"Hallo,\nbitte bestätigen sie Ihre Email\n{url}",
            from_email="info@gmail.com",
            recipient_list=[user.email]
        )
        # print("Url: ", url)


    def create_user(self, email, password=None, **extra_fields):
        """Methode zum Anlegen eines Standard Users"""
        # wird von API aufgerufen
        user = self.model(email=email, **extra_fields)
        user.email_token = uuid.uuid1()
        user.set_password(password)
        user.save(using=self._db)
        self.send_confirmation_mail(user)    
        return user
    
    def create_superuser(self, email, password=None):
        """Methode zum Anlegen eines Super Users"""
        # Wird direkt durch create superuser aufgerufen (shell)
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        USER = "User"
        MODERATOR = "Moderator"
        PREMIUM = "Premium"
        ADMIN = "Admin"

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True, null=True, blank=True)     # blank = leer im Formular, null = leer in Datenbank erlaubt
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    email_token = models.UUIDField(
        null=True, blank=True, editable=False
    )   # Zur Kontoverifizierung per Email
    email_confirmed = models.BooleanField(default=False, help_text="Der User hat seine Email Adresse verifiziert")
    objects = CustomUserManager()       # Jedes Modell braucht einen Manager (= Schnittstelle zur Datenbank)
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email