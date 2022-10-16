from rest_framework import serializers
from .models import Car, Owner, Roads, AllNodes, TollStation
from django.contrib.gis.geos import fromstr
from django.core.exceptions import MultipleObjectsReturned

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

    def validate_ownerCar(self, value):
        counter = 0
        for car in value:
            if car["type"] == "big": counter += 1
        if counter > 1 :
            raise serializers.ValidationError('Can`t have more than one big car')
        return value

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roads
        fields = ('name', 'width', 'geom')

class AllNodesSeializer(serializers.ModelSerializer):
    class Meta:
        model = AllNodes
        fields = ('car', 'location', 'date', 'road')

    def create(self, validated_data):
        point = fromstr(validated_data['location'])
        try:
            rd = Roads.objects.get(geom__contains=point)
            print(rd)
            
        except Roads.DoesNotExist :
            rd = None
        except MultipleObjectsReturned:
            rd = None
            
        validated_data['road'] = rd
        return AllNodes.objects.create(**validated_data)
              
class TollStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TollStation
        fields = ('name', 'toll_per_cross', 'location')
