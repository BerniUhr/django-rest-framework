from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoryListCreateView.as_view(), name="list-create-categories"),
    path('external', views.ExternalApiView.as_view(), name="external"),
    # curl http://127.0.0.1:8000/api/events/categories -H "Authorization: Token 0e51be3480c7a44ba30ea9079b1e21b43b057105"
    # curl -X POST http://127.0.0.1:8000/api/events/categories -H "Authorization: Token 0e51be3480c7a44ba30ea9079b1e21b43b057105" -d "name=superkat"
    # path('create', views.CreateUserView.as_view(), name="create-user"),
    # path('about', views.ManageUserView.as_view(), name="manage-user"),
    # path('confirm/<int:uid>/<str:confirm_token>', views.EmailconfirmationUserView.as_view(), name="confirm-user"),
]