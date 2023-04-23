"""URL mapping for user API

/api/user/
/api/user/create
/api/user/me/
"""

from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
]
