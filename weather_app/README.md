Django Weather App
Overview
This Django application integrates with the OpenWeatherMap API to fetch, store, and manage weather data for different cities. It uses PostgreSQL as the database and Celery for background tasks to periodically update weather data.

Features
External API Integration: Fetch weather data from the OpenWeatherMap API.
CRUD Operations: Basic Create, Read, Update, and Delete operations for weather data.
Background Jobs: Periodically update weather data for specified cities using Celery.
Docker Support: Includes Dockerfile and docker-compose.yml for easy setup and deployment.
Setup
Prerequisites
Docker and Docker Compose: Ensure Docker and Docker Compose are installed on your machine.
OpenWeatherMap API Key: Obtain an API key from OpenWeatherMap and replace the placeholder in weather/utils.py.
Configuration

Clone the Repository:

git clone https://github.com/kmallikarjun806/weather_pro/pull/new/development

cd your-repo
Set Up Environment Variables:

Replace your_openweathermap_api_key in weather/utils.py with your actual API key.
Update the database credentials in docker-compose.yml if necessary.
Build and Run Docker Containers:

docker-compose build
docker-compose up
Apply Database Migrations:


docker-compose exec web python manage.py migrate
API Endpoints:

1.Fetch Weather Data for a City
Endpoint: GET /api/weather/{city}/
Description: Fetch and return the latest weather data for the specified city from the database.

2. Response Example:

{
  "id": 1,
  "city": "London",
  "temperature": 15.5,
  "description": "Clear sky",
  "timestamp": "2024-07-09T12:00:00Z"
}

2. Update Weather Data for a City

Endpoint: POST /api/weather/{city}/update/
Description: Fetch the latest weather data from the external API for the specified city and store it in the database.
Response Example:
json
Copy code
{
  "id": 1,
  "city": "London",
  "temperature": 15.5,
  "description": "Clear sky",
  "timestamp": "2024-07-09T12:00:00Z"
}


3. Fetch All Stored Weather Data

Endpoint: GET /api/weather/
Description: Return all stored weather data.

Response Example:

[
  {
    "id": 1,
    "city": "London",
    "temperature": 15.5,
    "description": "Clear sky",
    "timestamp": "2024-07-09T12:00:00Z"
  },
  {
    "id": 2,
    "city": "New York",
    "temperature": 25.0,
    "description": "Sunny",
    "timestamp": "2024-07-09T12:00:00Z"
  }
]


4. Update Weather Data Entry
Endpoint: PUT /api/weather/{id}/
Description: Update the weather data entry with the specified ID.
Request Body Example:

{
  "temperature": 16.0,
  "description": "Partly cloudy"
}
Response Example:

{
  "id": 1,
  "city": "London",
  "temperature": 16.0,
  "description": "Partly cloudy",
  "timestamp": "2024-07-09T12:00:00Z"
}


5. Delete Weather Data Entry
Endpoint: DELETE /api/weather/{id}/delete/
Description: Delete the weather data entry with the specified ID.
Response Example:

{
  "message": "Weather data with ID 1 has been deleted."
}



Background Jobs
Celery is used to periodically update weather data for the cities London and New York. By default, it updates every 10 minutes. Ensure Redis is running as the message broker for Celery.

Celery Commands

Start Celery Worker:

-docker-compose up celery



Start Celery Beat Scheduler:

-docker-compose up celery-beat