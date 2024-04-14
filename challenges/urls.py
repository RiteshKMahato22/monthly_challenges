from django.urls import path
from . import views

urlpatterns = [
    path("january",views.month1),
    path("february",views.month2),
    path("march",views.month3),
]