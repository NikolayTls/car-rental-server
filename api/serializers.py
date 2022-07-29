from rest_framework import serializers
from base.models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name','city']
        depth = 1

class ReservationSerializer(serializers.ModelSerializer):
    car = serializers.ReadOnlyField(source='car.name')
    city = serializers.ReadOnlyField(source='city.name')
    station = serializers.ReadOnlyField(source='station.name')
    city1 = serializers.ReadOnlyField(source='city1.name')
    station1 = serializers.ReadOnlyField(source='station1.name')
    pickup_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    dropoff_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 1 

class CreateReservationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Reservation
            fields = ['id','car','city','station','city1','station1','pickup_date','dropoff_date','price']
            depth = 1

