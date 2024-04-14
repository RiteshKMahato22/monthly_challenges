from django.urls import path
from . import views

urlpatterns = [
    path("<text>",views.monthly_challenge)
]