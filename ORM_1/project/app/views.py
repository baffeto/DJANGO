from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Person
import random


def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']), 
        model=random.choice(['M1', 'M2', 'M3']), 
        color=random.choice(['C1', 'C2', 'C3'])
    ) # Объект существует лишь в памяти нашей базы данных
    
    car.save() # Запись появляется в БД
    return HttpResponse(f"Все получилось! Новая машина: {car.brand}, {car.model}")

def list_car(request):
    car_objects = Car.objects.all() # Получаем все объекты
    cars = [f'{c.id} | {c.brand} | {c.model} | {c.color} | {c.owners.count()}' for c in car_objects] # Превращаем в строки
    return HttpResponse('<br>'.join(cars))

def filter_car(request):
    # car_objects = Car.objects.filter(brand='B1')
    # car_objects = Car.objects.filter(brand__contains='2') # Чтобы содержал 2
    car_objects = Car.objects.filter(brand__startswith='2') # Чтобы начиналась с 2
    cars = [f'{c.id} | {c.brand} | {c.model} | {c.color}' for c in car_objects] # Превращаем в строки
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Два варианта создания записи в базу данных
        
        # Person(name='P', car=car).save()
        Person.objects.create(name='P', car=car)
    return HttpResponse('Все получилось!')


def list_person(request):
    person_objects = Person.objects.all()
    persons = [f'{person.id} | {person.name} | {person.car}' for person in person_objects]
    return HttpResponse(f'<br>'.join(persons))