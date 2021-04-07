from django.apps import AppConfig
from django.urls import path
from . import views


class MysuperheroesConfig(AppConfig):
    name = 'mysuperheroes'


app_name = 'superheroes'
urlpatterns = [
    path('index', views.index, name='index')
]

