from django.contrib import admin
from django.urls import path
from . import views


app_name = 'mysuperheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mysuperheros_id>/', views.detail, name='detail'),
    path('new/', views.create, name='new')

]