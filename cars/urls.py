from django.urls import path
from cars.views import CarListView

urlpatterns = [
    path('car_list/', CarListView.as_view())
]

