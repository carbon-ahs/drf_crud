from django.urls import path
from .api import StudentApi
from . import views

urlpatterns = [
    # path("", views.site_home, name="home"),
    path("", StudentApi.as_view()),
]
