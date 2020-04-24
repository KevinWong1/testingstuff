import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
import glob
import os
from django import forms

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

class BlogPostForm(forms.Form):
        name = forms.CharField(max_length=100)
        post = forms.CharField(max_length=100)
        time = forms.CharField(max_length=100)
        date = forms.CharField(max_length=100)



from .models import Blog

def add_blog_post(request):
    context = {}
    # First, check if they have submitted something:
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
        # Then, get the name out of the POST dictionary
            name = form.cleaned_data['name']
            post = form.cleaned_data['post']
            time = form.cleaned_data['time']
            date = form.cleaned_data['date']

        # Finally, actually create the appointment
            Blog.objects.create(
                name=name,
                date=date,
                time=time,
                post = post,
            )

            return redirect('/blog-posts')
    else:
        form = BlogPostForm
    context = {
        'form': form,
    }

    return render(request, 'add_blog_post.html', context)

def view_blog_post(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog_posts.html', context)


def blog(request):
    context = {
    "title": "blog",
    "year": str(year),
    "pages": pages,
    }
    return render(request, "content/blog.html", context)

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
