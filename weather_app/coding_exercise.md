# Coding Task: Django Application with External API Integration, PostgreSQL, and Celery

## Task Description:
Create a Django application that integrates with a public API, retrieves data, and stores it in a PostgreSQL database. The application should expose endpoints to fetch the stored data and perform basic CRUD operations.

## Requirements:

### 1. **External API Integration:**
  - Use a public API (e.g., OpenWeatherMap API) to fetch weather data for a given city.
  - Store the fetched data in a PostgreSQL database.

### 2. **Database Schema:**
  - Create a PostgreSQL database schema to store the weather data. The schema should include fields such as city name, temperature, weather description, and timestamp.

### 3. **Endpoints:**

  - **GET /weather/{city}:** Fetch and return the latest weather data for the specified city from the database.
  - **POST /weather/{city}:** Fetch the latest weather data from the external API for the specified city and store it in the database.
  - **GET /weather:** Return all stored weather data.
  - **PUT /weather/{id}:** Update the weather data entry with the specified ID.
  - **DELETE /weather/{id}:** Delete the weather data entry with the specified ID.

### 4. **Background Jobs:**
  - Implement a background job using Celery to periodically fetch and update the weather data for a list of cities (`London` and `New York`).

### 5. **Code Quality:**
  - Ensure the code is clean, well-documented, and follows best practices (e.g., PEP 8 guidelines).
  - Include error handling and validation.

## Deliverables:
1. Django application code.
2. PostgreSQL database schema.
3. Documentation on how to set up and run the application.
4. Example requests and responses for the endpoints.
5. Dockerfile and docker-compose.yml for easy setup (optional but preferred).
6. Swagger (OpenAPI) docs (optional but preferred).

## Weather API:

Create an API token for the OpenWeatherMap API ((link)[https://openweathermap.org/api]) and use it to fetch weather data for a city.

**Fetch weather data:**

```http
GET /weather/{city}
```

Response:

```json
{
  "city": "London",
  "temperature": 15.5,
  "description": "Clear sky",
  "timestamp": "2024-07-09T12:00:00Z"
}
```

**Store weather data for a city:**

```http
GET /weather/{city}
```

Response:

```json
{
  "message": "Weather data for London has been updated."
}
```

**Fetch all weather data:**

```http
GET /weather
```

Response:

```json
[
  {
    "city": "London",
    "temperature": 15.5,
    "description": "Clear sky",
    "timestamp": "2024-07-09T12:00:00Z"
  },
  {
    "city": "New York",
    "temperature": 25.0,
    "description": "Sunny",
    "timestamp": "2024-07-09T12:00:00Z"
  }
]
```

**Update weather data:**

```http
PUT /weather/{id}
```

Response:

```json
{
  "temperature": 16.0,
  "description": "Partly cloudy"
}
```

**Delete weather data:**

```http
DELETE /weather/{id}
```

Response:

```json
{
  "message": "Weather data with ID 1 has been deleted."
}
```
