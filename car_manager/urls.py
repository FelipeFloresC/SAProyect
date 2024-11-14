from django.urls import path
from .views import CreateMetricsView
urlpatterns=[
    path('create-metrics/', CreateMetricsView.as_view(), name='create-metrics'),
]