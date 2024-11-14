# car_manager/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from .mailer import send_stolen_car_alert

@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    if created:
        send_stolen_car_alert(instance.id)
