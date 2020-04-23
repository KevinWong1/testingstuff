import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import glob
import os


pages = []
all_content_files = glob.glob("app/templates/content/*.html")
for page in all_content_files:
    file_name = os.path.basename(page)
    name_only, extension = os.path.splitext(file_name)
    pages.append({
        "filename": "content/" + file_name,
        "title": name_only,
        "output": file_name
    })
year = datetime.datetime.now().strftime('%Y')

def index(request):
    context = {
    "title": "index",
    "year": str(year),
    "pages": pages,
    }
    return render(request, "content/index.html", context)

def about(request):
    context = {
    "title": "about",
    "year": str(year),
    "pages": pages,
    }
    return render(request, "content/about.html", context)

def projects(request):
    context = {
    "title": "projects",
    "year": str(year),
    "pages": pages,
    }
    return render(request, "content/projects.html", context)

# API call:
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state},{country code}&appid={your api key}
# don't take my key :(
api_key = "e48e0a2d37211056d27243de4d6d61eb"
url = 'https://api.openweathermap.org/data/2.5/weather?q=Oakland,California,USA&units=metric&APPID='+ api_key
weather_icon_start = 'http://openweathermap.org/img/wn/'
weather_icon_end = '.png'

def weather(request):
    time_now = datetime.datetime.now()
    response = requests.get(url)
    jsons = response.json()

    weather_icon_middle = jsons['weather'][0]['icon']
    weather_icon = weather_icon_start + weather_icon_middle + weather_icon_end
    context = {
        "icon": weather_icon,
        "temp": jsons['main']['temp'],
        "weather": jsons['weather'][0]['description'],
        "current_time": time_now,
        "temp_in_F": (jsons['main']['temp'] * 9/5) + 32
    }
    return render(request, "weather_template.html", context)
