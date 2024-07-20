from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import fetch_weather_data

@api_view(['GET'])
def get_weather(request, city):
    weather_data = WeatherData.objects.filter(city=city).order_by('-timestamp').first()
    if not weather_data:
        return Response({"error": "Weather data for the city not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = WeatherDataSerializer(weather_data)
    return Response(serializer.data)

@api_view(['POST'])
def update_weather(request, city):
    data = fetch_weather_data(city)
    weather_data, created = WeatherData.objects.update_or_create(
        city=city,
        defaults={'temperature': data['temperature'], 'description': data['description']}
    )
    serializer = WeatherDataSerializer(weather_data)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_weather(request):
    weather_data = WeatherData.objects.all()
    serializer = WeatherDataSerializer(weather_data, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_weather_entry(request, id):
    weather_data = get_object_or_404(WeatherData, id=id)
    serializer = WeatherDataSerializer(weather_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_weather_entry(request, id):
    weather_data = get_object_or_404(WeatherData, id=id)
    weather_data.delete()
    return Response({"message": "Weather data with ID {} has been deleted.".format(id)}, status=status.HTTP_204_NO_CONTENT)
