from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    city = request.POST.get('city', 'Bangalore')
    
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b9fcc03b7d3186728f623782e342f58d'
    weather_params = {'units': 'metric'}
    
    google_api_key = 'AIzaSyCJVl3C_F6MYJGFGZG_UFJPj1N6gq3_UZY'
    search_engine_id = 'f73e5dc15a87348fb'
    query = f"{city} 1920x1080"
    start = 1
    search_type = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={search_engine_id}&q={query}&start={start}&searchType={search_type}&imgSize=xxlarge"
    
    try:
        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()
        
    except (requests.exceptions.RequestException, KeyError) as e:
        messages.error(request, 'Weather data is not available for the entered city.')
        description = 'clear sky'
        icon = '01d'
        temp = 25
        day = datetime.date.today()
        city = 'Bangalore'
    
    try:
        image_response = requests.get(city_url)
        image_response.raise_for_status()
        image_data = image_response.json()
        search_items = image_data.get('items', [])
        if search_items:
            image_url = search_items[0]['link']
        else:
            image_url = None
        
    except (requests.exceptions.RequestException, KeyError) as e:
        messages.error(request, 'Image data is not available for the entered city.')
        image_url = None
    
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'exception_occurred': 'exception_occurred' in locals(),
        'image_url': image_url,
    }
    
    return render(request, 'index.html', context)
