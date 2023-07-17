from django.contrib import admin
from django.urls import path
from app.views import create_car, list_car, filter_car, create_person, list_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', list_car),
    path('new_car/', create_car),
    path('car_filter/', filter_car),
    path('new_person/', create_person),
    path('persons/', list_person)
]
