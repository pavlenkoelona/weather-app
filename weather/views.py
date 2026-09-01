import os

import requests
from django.shortcuts import render


def weather_view(request):
    city = request.GET.get("city", "London").strip() or "London"
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return render(
            request,
            "weather/weather.html",
            {"city": city, "error": "Weather service is not configured."},
        )

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=5,
        )
        data = response.json()
    except (requests.RequestException, ValueError):
        return render(
            request,
            "weather/weather.html",
            {"city": city, "error": "Weather service is temporarily unavailable."},
        )

    if response.status_code == 200:
        context = {
            "city": data.get("name", city),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "weather_type": data["weather"][0]["main"].lower(),
        }
    else:
        context = {"city": city, "error": "City not found."}

    return render(request, "weather/weather.html", context)
