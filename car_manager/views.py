from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Message, Car
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MetricsSerializer
from django.shortcuts import get_object_or_404
import json

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
        try:
            user = get_object_or_404(User, id=request.data.get('user'))
            car = get_object_or_404(Car, id=request.data.get('car'))
            
            data = request.data.get('data')
            if isinstance(data, dict):
                data = json.dumps(data)
            
            serializer = MetricsSerializer(data={
                'user': user.id,
                'car': car.id,
                'data': data
            })
            
            if serializer.is_valid():
                metrics = serializer.save()
                return Response({
                    "message": "Metrics created successfully",
                    "id": metrics.id
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "error": "Invalid data",
                "details": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)