from django.urls import path
from . import views



urlpatterns = [
    path('',views.getData),
    path('add/', views.addCar),
    path('reservations/', views.getReservations),
    path('reservation-create/',views.reservationCreate),
    path('reservation-update/<str:pk>/', views.reservationUpdate),
    path('reservation-delete/<str:pk>/', views.reservationDelete),
    path('cities/', views.getCities),
    path('stations/', views.getStations),
    path('ajax/load-stations/<str:pk>', views.ajaxStation),
    path('reservation/<str:pk>/',views.getReservation)


]