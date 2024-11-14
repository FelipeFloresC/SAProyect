from django.urls import path
from .views import CreateMetricsView
from . import views

urlpatterns = [
    path('test-mailer/', views.test_mailer, name='test-mailer'),
    path('create-metrics/', CreateMetricsView.as_view(), name='create-metrics'),

]