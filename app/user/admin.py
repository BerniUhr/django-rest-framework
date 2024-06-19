from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """ Eigene Klasse in der Admin anzeigen lassen """
    list_display = ["id", "user_name", "email", "is_active", "is_staff", "role", "email_confirmed"]
    ordering = ["email"]
    readonly_fields = ["email_confirmed"]

    # anzeige Fieldset
    fieldsets = (
        (None, {"fields": ("password", "user_name")}),
        ("Personal info", {"fields": ("email", "role", "email_confirmed")}), 
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        # ("Important dates", {"fields": ("last_login",)}),  # , "date_joined"
        # ("Additional info", {"fields": ("address",)}),
    )

    add_fieldsets = (
        (None, {"fields": ("password1", "password2")}),
        ("Personal info", {"fields": ("email", "role", "email_confirmed")}),  # "first_name", "last_name",
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        # ("Important dates", {"fields": ("last_login",)}),  # , "date_joined"
        # ("Additional info", {"fields": ("address",)}),
    )