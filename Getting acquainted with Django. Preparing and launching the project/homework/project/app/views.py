from django.shortcuts import render
import datetime 
from django.http import HttpResponse
import os

# Create your views here.

# Вывод всех страниц
def index(request):    
    return render(request=request, template_name='main.html')

def time(request):
    time_now = datetime.datetime.now().time()
    return HttpResponse(f'Время: {time_now}')

def workdir(request):
    context = {'files': os.listdir(path='.')}
    return render(request=request, template_name='workdir.html', context=context)