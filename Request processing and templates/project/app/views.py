from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse(f'{settings.DEBUG}, свяжитесь с нашим админом!')

def hello(request):
    name = request.GET.get("name", "Пользователь")
    age = request.GET.get("age", 20)
    return HttpResponse(f'Hello! {name}\nYou {age}')

def sum(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')

def date(request, dt):
    return HttpResponse(f'Время: {dt}')

def template(request):
    context = {
        'task': 6,
        'data': [1, 5, 8],
        'val': 'hello'
    }
    return render(request=request,
                  template_name='demo.html', context=context)
    
CONTENT = [str(i) for i in range(10000)]
    
def pagination(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request=request, template_name='pagination.html', context=context)