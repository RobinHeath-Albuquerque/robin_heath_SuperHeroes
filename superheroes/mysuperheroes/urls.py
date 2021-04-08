from django.contrib import admin
from django.http import request
from django.urls import path
from . import views


app_name = 'mysuperheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='new'),
        path('', views.delete, name='delete')

]




