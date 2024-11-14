from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Message
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_mailer(request):
    try:
        # Get or create a test user
        user, created = User.objects.get_or_create(
            username='juan',
            defaults={
                'email': 'samailerx@gmail.com',
            }
        )
        
        # Create a test message
        message = Message.objects.create(
            user=user,
            patente='TEST12',
            csv='test data'
        )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Test message created with ID: {message.id}'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })