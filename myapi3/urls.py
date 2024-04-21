from django.urls import path
from . import views
urlpatterns=[
    path("",views.obj_removal,name="obj_removal")
]