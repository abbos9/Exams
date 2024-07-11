from django.urls import path
from wather.views import index, history_search

urlpatterns = [
    path('', index),
    path('history/', history_search)
]