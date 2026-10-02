from django.urls import path
from cars.views import car_list_view

urlpatterns = [
    path('car_list/', car_list_view)
]

