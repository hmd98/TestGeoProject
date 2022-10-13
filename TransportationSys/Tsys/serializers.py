from dataclasses import fields
from rest_framework import serializers
from .models import Car, Owner, Roads, AllNodes

class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ('id', 'type', 'color', 'length', 'load_valume')

class OwnerSerializer(serializers.ModelSerializer):
    ownerCar = CarSerializer(many=True)
    class Meta:
        model = Owner
        fields = ('name', 'national_code', 'age', 'total_toll_paid', 'ownerCar')

    def create(self, validated_data):
        car_data = validated_data.pop('ownerCar')
        owner = Owner.objects.create(**validated_data)
        for car in car_data:
            Car.objects.create(owner=owner, **car)
        return owner

class AllNodesSeializer(serializers.ModelSerializer):
    class Meta:
        model = AllNodes
        fields = ('car', 'location', 'date')


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roads
        fields = ('name', 'width', 'geom')