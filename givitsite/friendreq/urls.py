from django.urls import path

from . import views

urlpatterns = [
    path('', views.itemRequest_create_view, name = 'itemRequest_create_view'),
]
