from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Car,City,Station,Reservation
from .serializers import *

from django.http import JsonResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET'])
def getData(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars,many = True)

    return Response(serializer.data)

@api_view(['POST'])
def addCar(request):

    serializer = CarSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

@api_view(['GET'])
def getReservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getReservation(request,pk):
    reservation = Reservation.objects.get(id = pk)

    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

@api_view(['POST'])
def reservationCreate(request):
    reservation_data = request.data

    carId = Car.objects.get(name = reservation_data["car"]).id
    cityId = City.objects.get(name = reservation_data["city"]).id
    stationId = Station.objects.get(name = reservation_data["station"]).id
    city1Id = City.objects.get(name = reservation_data["city1"]).id
    station1Id = Station.objects.get(name = reservation_data["station1"]).id

    new_reservation = Reservation.objects.create(car = Car.objects.get(id = carId), city= City.objects.get(id = cityId), station = Station.objects.get(id = stationId),
    pickup_date = reservation_data["pickup_date"],city1= City.objects.get(id = city1Id), station1 = Station.objects.get(id = station1Id), dropoff_date = reservation_data["dropoff_date"],
    price = reservation_data["price"])

    new_reservation.save()
    serializer = CreateReservationSerializer(new_reservation)
    return Response(serializer.data)

@api_view(['PATCH'])
def reservationUpdate(request,pk):
    reservation = Reservation.objects.get(id = pk)

    data = request.data

    car = Car.objects.get(name = data["car"])
    city = City.objects.get(name = data["city"])
    city1 = City.objects.get(name = data["city1"])
    station = Station.objects.get(name = data["station"])
    station1 = Station.objects.get(name = data["station1"])



    reservation.car = car
    reservation.city = city
    reservation.station = station
    reservation.city1 = city1
    reservation.station1 = station1
    reservation.price = data["price"]
    reservation.pickup_date = data["pickup_date"]
    reservation.dropoff_date = data["dropoff_date"]

    reservation.save()

    serializer = CreateReservationSerializer(reservation)
    return Response(serializer.data)


@api_view(['DELETE'])
def reservationDelete(request, pk):
    reservation = Reservation.objects.get(id = pk)
    reservation.delete()

    return Response("Deleted successfully")


@api_view(['GET'])
def getCities(request):
    cities = City.objects.all()

    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStations(request):
    stations = Station.objects.all()

    serializer = StationSerializer(stations, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def ajaxStation(request,pk):
    city_id = pk
    stations = Station.objects.filter(city_id=city_id).order_by('name')

    serializer = StationSerializer(stations, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        'api/token/refresh'
    ]

    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer