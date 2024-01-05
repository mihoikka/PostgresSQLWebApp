from django.urls import path

from . import views

urlpatterns = [
    path("updatepage", views.updatepage, name="updatepage"),
    path("updatechar", views.updateChar, name="updateChar"),
    ]