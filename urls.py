from django.contrib import admin
from django.urls import path
from maketrip import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('flights/', views.flights_page, name='flights'),
    path('hotels/', views.hotels_page, name='hotels'),
    path('search/', views.search_results, name='search'),
]
