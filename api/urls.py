from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # Can generate token for users (body (username, password))

from .views import HelloView, EventView

app_name = "events"

urlpatterns = [
    path('hello/', HelloView.as_view(), name="hello_world"),
    path('create-event/', EventView.as_view(), name="create_event"),
    path('get-token/', obtain_auth_token, name="generate_token")
]
