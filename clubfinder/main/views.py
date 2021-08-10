from django.shortcuts import render
from django.http.response import HttpResponse
import requests, json
import os
from geopy.geocoders import Nominatim
from .models import *

def index(response):
    activity = ''
    if response.method == "POST":
        activity = response.POST.getlist('activityResult')[0]
        if activity == 'Business / Finance':

            business_list = list(Business.objects.all())
            # q = Business.objects.filter(name='JA Southern Alberta')[0].name
            print(business_list)


    return render(response, 'main/index.html', {})

def map(response):
    return render(response, 'main/map.html', {})
