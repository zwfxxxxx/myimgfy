from django.urls import path
from . import views
urlpatterns = [
    path("", views.process_image,name="process_image")
]
# urlpatterns = [
#     path("", views.process_image,name="process_image"),
#     # path("", views.Background_removal,name = "Background_removal")
# ]