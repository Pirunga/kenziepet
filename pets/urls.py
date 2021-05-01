from django.urls import path
from pets.views import AnimalView

urlpatterns = [
    path("animals/", AnimalView.as_view()),
]
