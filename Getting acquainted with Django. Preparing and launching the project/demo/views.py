from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return HttpResponse('Hello from django!')

def time(request):
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Time = {current_time}')