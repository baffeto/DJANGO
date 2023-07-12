from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('omlet/', views.omlet),
    path('pasta/', views.pasta),
    path('buter/', views.buter)
]
