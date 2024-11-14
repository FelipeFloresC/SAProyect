from django.contrib import admin
from .models import Car, Message, Metrics

admin.site.register(Car)
admin.site.register(Message)
admin.site.register(Metrics)