from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Message, Car
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MetricsSerializer

@csrf_exempt
def test_mailer(request):
    try:
        user, created = User.objects.get_or_create(
            username='juan',
            defaults={
                'email': 'samailerx@gmail.com',
            }
        )
        
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

class CreateMetricsView(APIView):
    def post(self, request):
        serializer = MetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
