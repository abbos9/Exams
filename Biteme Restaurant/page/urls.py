from django.urls import path
from page.views import PageHomeView, PageReservationView, PageSubscribeView
app_name = 'pages'

urlpatterns = [
    path('', PageHomeView, name='home' ),
    path('reservation/', PageReservationView.as_view(), name='reservation'),
    path('subscribe/', PageSubscribeView, name='subscribe'),
]