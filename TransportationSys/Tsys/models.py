from random import choices
from django.contrib.gis.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=255)
    national_code = models.IntegerField()
    age = models.IntegerField()
    total_toll_paid = models.IntegerField()

class Car(models.Model):
    CHOICES = [
        ('Big', 'big'),
        ('Small', 'small')
    ]
    type = models.CharField(choices=CHOICES)
    color = models.CharField()
    length = models.FloatField()
    load_valume = models.FloatField()
    owner = models.ForeignKey(Owner, related_name='ownerCar')


class Roads(models.Model):
    name = models.CharField(max_length=255)
    width = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

class TollStation(models.Model):
    name = models.CharField(max_length=255)
    toll_per_cross = models.IntegerField()
    location = models.PointField(srid=4326)

class AllNodes(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    location = models.PointField(srid=4326)
    date = models.DateTimeField()