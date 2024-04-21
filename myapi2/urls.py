from django.urls import path
from . import views
urlpatterns = [
    path("", views.background_removal,name="background_removal")
]