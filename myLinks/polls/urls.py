from django.urls import path

from . import views
from .Views import LoginPage

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginPage.login , name='index'),
]