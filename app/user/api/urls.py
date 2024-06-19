from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.ListUserView.as_view(), name="list-users"),
    path('create', views.CreateUserView.as_view(), name="create-user"),
    path('about', views.ManageUserView.as_view(), name="manage-user"),
    path('token', obtain_auth_token, name="token"),     # obtain_auth_token(request) --> HttpResponse
    # curl -X POST -d "username=info@example.com" -d "password=12345" http://127.0.0.1:8000/api/users/token
    # http://127.0.0.1/api/users/confirm/8/2fc9a338-2caf-11ef-8af3-8469930c56a7
    path('confirm/<int:uid>/<str:confirm_token>', views.EmailconfirmationUserView.as_view(), name="confirm-user"),
]