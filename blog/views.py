from django.shortcuts import render
from django.http import HttpResponse


def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('Ура это первый мой проект на DJANGO')

def my_favourite_emodji_view(request):
    if request.method == "GET":
        return HttpResponse('😁🤣🤖🫠🌚')

def about_my_self_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Радомир, я BACKEND DEVELOPER')