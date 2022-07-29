from django.urls import path
from . import views
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



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
    path('reservation/<str:pk>/',views.getReservation),
    path('api/',views.getRoutes),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')


]