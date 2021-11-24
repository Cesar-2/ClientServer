# Django config'
from django.urls import path
from to_do.views import CardAPI

urlpatterns = [
    path('Card', CardAPI.as_view()),
]
