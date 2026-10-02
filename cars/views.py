from django.shortcuts import render
from cars.models import Car


def car_list_view(request):
    if request.method == 'GET':
        car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car})