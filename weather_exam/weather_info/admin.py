from django.contrib import admin
from weather_info.models import Weather, History
# Register your models here.

admin.site.register(Weather)
admin.site.register(History)