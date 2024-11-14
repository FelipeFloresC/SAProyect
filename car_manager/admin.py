from django.contrib import admin
from .models import Car
from .models import Message

admin.site.register(Car)
admin.site.register(Message)