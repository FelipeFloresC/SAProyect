from django.core.mail import send_mail
from django.conf import settings
from car_manager.models import Message
import logging

logger = logging.getLogger(__name__)

def send_stolen_car_alert(message_id):
    try:
        message = Message.objects.get(id=message_id)
        
        if message.patente.upper().startswith('TEST'):
            subject = f"Alert: Car {message.patente} reported as stolen"
            body = f"Dear {message.user.username},\n\n" \
                   f"Your car with license plate {message.patente} has been flagged with unusual values. " \
                   f"Timestamp: {message.timestamp}.\n\n" \
                   f"Your car will stop immediately.\n\nBest regards,\nYour Car Manager Team"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [message.user.email]

            try:
                send_mail(
                    subject,
                    body,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                logger.info(f"Test alert email sent to {message.user.username} for car {message.patente}")
                print(f"Email sent successfully to {message.user.email}")
            except Exception as e:
                logger.error(f"Failed to send email: {str(e)}")
                print(f"Failed to send email: {str(e)}")
                raise 
                
    except Message.DoesNotExist:
        logger.error(f"Message with id {message_id} does not exist")
    except Exception as e:
        logger.error(f"Unexpected error in send_stolen_car_alert: {str(e)}")