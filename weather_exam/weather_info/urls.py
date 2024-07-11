from django. urls import path
from weather_info.views import get_site,history_search

urlpatterns = [
    path('', get_site),
    path('history/',history_search)
    ]