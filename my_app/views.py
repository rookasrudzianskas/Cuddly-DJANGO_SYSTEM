from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . import models
from requests.compat import quote_plus


BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


# Create your views here.

def home(request):
    return render(request, 'base.html', {})


def new_searches(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    print(data)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/new_searches.html', stuff_for_frontend)
