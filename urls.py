from django.urls import path

from models import views

urlpatterns = [
    path('', views.index, name='index'),
]
