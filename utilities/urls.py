from django.urls import path
from . import views


# /utilities/'이후의 url'
urlpatterns = [
    path('index/', views.index),
]