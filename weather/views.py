import requests
from django.shortcuts import render

def weather_view(request):
    api_key = "3913a1047e172baee439b5b49a3f5ddd"  # Clave temporal válida
    city = request.GET.get("city", "London")  # Ciudad por defecto
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "weather_type": data["weather"][0]["main"].lower()  # Ej: "clear", "rain"
        }
    else:
        weather_data = {
            "city": city,
            "error": "City not found",
            "status_code": response.status_code  # Para depurar
        }
    
    return render(request, "weather/weather.html", weather_data)