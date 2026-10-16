from django.shortcuts import render
from cars.models import Car
from django.views import generic

class CarListView(generic.ListView):
    template_name = 'car_list.html'
    model = Car
    context_object_name = 'car'
    ordering = ['-id']
    

# def car_list_view(request):
#     if request.method == 'GET':
#         car = Car.objects.all()
#     return render(request, 'car_list.html', {'car': car})