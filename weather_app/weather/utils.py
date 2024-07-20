import requests
from datetime import datetime

def fetch_weather_data(city):
    api_key = 'Add api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    return {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'timestamp': datetime.fromtimestamp(data['dt'])
    }
