from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.get_weather),
    path('weather/<str:city>/update/', views.update_weather),
    path('weather/', views.get_all_weather),
    path('weather/<int:id>/', views.update_weather_entry),
    path('weather/<int:id>/delete/', views.delete_weather_entry),
]
