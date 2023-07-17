from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = []
    page_number = int(request.GET.get("page", 1))
    
    with open("C:\\Users\\Gorob\\Desktop\\DJANGONETOLOGY\\Request processing and templates\\pagination\\project\\app\\data\\data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            data_2 = data.append([row[0], row[4], row[6]])
            
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    
    context = {
        'page': page
    }
    
    return render(request, 'index.html', context)