# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) #Many-to-One relationship
    dealer_id = models.IntegerField(null=True, blank=True) #allows dealer_id to be 
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=datetime.datetime.now().year,
        validators=[
            MaxValueValidator(datetime.datetime.now().year),
            MinValueValidator(2015)
        ]
    )
    color = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.car_make.name} - {self.name}"