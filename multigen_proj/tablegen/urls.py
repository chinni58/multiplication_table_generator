# tablegen/urls.py
from django.urls import path
from . import views

app_name = 'tablegen'

urlpatterns = [
    path('', views.index, name='index'),
]
