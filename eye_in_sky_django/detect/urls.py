from django.urls import path, include
from . import views

urlpatterns=[
    path('home/',views.call,name="start"),
    path('stop/',views.stop, name="stop")
]