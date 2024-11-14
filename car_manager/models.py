from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    patente = models.CharField(max_length=20, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.owner.username}"
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patente = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    csv = models.FileField(upload_to='uploads/csv_files/')

    """ def __str__(self):
        return f"El auto con patente {self.patente} perteneciente al usuario
                {self.user.username} ha detectado valores extraños {self.csv}, a las {self.timestamp}" """
    
class Metrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    speed = models.FloatField()  
    fuel_level = models.FloatField()  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Metrics for {self.user.username} - {self.car.patente} at {self.timestamp}"