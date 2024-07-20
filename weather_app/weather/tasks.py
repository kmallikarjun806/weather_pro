from celery import shared_task
from .utils import fetch_weather_data
from .models import WeatherData

@shared_task
def update_weather_data():
    cities = ['London', 'New York']
    for city in cities:
        data = fetch_weather_data(city)
        WeatherData.objects.update_or_create(
            city=city,
            defaults={
                'temperature': data['temperature'],
                'description': data['description'],
                'timestamp': data['timestamp']
            }
        )
