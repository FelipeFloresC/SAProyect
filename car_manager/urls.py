from django.urls import path
from . import views

urlpatterns = [
    path('test-mailer/', views.test_mailer, name='test-mailer'),
]