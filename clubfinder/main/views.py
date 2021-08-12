from django.shortcuts import render
from django.http.response import HttpResponse
import requests, json
import os
from geopy.geocoders import Nominatim
from .models import *

activity = ''

def index(response):
    names = []
    descriptions = []
    addresses = []
    lists = []
    global activity
    if response.method == "POST":
        activity = response.POST.getlist('activityResult')[0]
        if activity == 'Business / Finance':
            for i in range(Business.objects.count()):
                names.append(Business.objects.all()[i].name)
                descriptions.append(Business.objects.all()[i].description)
                addresses.append(Business.objects.all()[i].address)
        
        if activity == 'Public Speaking':
            for i in range(PublicSpeaking.objects.count()):
                names.append(PublicSpeaking.objects.all()[i].name)
                descriptions.append(PublicSpeaking.objects.all()[i].description)
                addresses.append(PublicSpeaking.objects.all()[i].address)

        if activity == 'Sports':
            for i in range(Sports.objects.count()):
                names.append(Sports.objects.all()[i].name)
                descriptions.append(Sports.objects.all()[i].description)
                addresses.append(Sports.objects.all()[i].address)

        if activity == 'STEM':
            for i in range(STEM.objects.count()):
                names.append(STEM.objects.all()[i].name)
                descriptions.append(STEM.objects.all()[i].description)
                addresses.append(STEM.objects.all()[i].address)
        
        if activity == 'Summer Camps and Programs':
            for i in range(SummerCamps.objects.count()):
                names.append(SummerCamps.objects.all()[i].name)
                descriptions.append(SummerCamps.objects.all()[i].description)
                addresses.append(SummerCamps.objects.all()[i].address)
        
        if activity == 'Tutoring':
            for i in range(Tutoring.objects.count()):
                names.append(Tutoring.objects.all()[i].name)
                descriptions.append(Tutoring.objects.all()[i].description)
                addresses.append(Tutoring.objects.all()[i].address)

        if activity == 'Youth Employment/Volunteering':
            for i in range(YouthEmployment.objects.count()):
                names.append(YouthEmployment.objects.all()[i].name)
                descriptions.append(YouthEmployment.objects.all()[i].description)
                addresses.append(YouthEmployment.objects.all()[i].address)
        
        lists = zip(names, descriptions, addresses)

    return render(response, 'main/index.html', {'lists':lists})

def map(response):
    adr = ''
    name = response.GET.get('name')

    if activity == 'Business / Finance':
        desc = Business.objects.filter(name=name)[0].description
        adr = Business.objects.filter(name=name)[0].address
    if activity == 'Public Speaking':
        desc = PublicSpeaking.objects.filter(name=name)[0].description
        adr = PublicSpeaking.objects.filter(name=name)[0].address
    if activity == 'Sports':
        desc = Sports.objects.filter(name=name)[0].description
        adr = Sports.objects.filter(name=name)[0].address
    if activity == 'STEM':
        desc = STEM.objects.filter(name=name)[0].description
        adr = STEM.objects.filter(name=name)[0].address
    if activity == 'Summer Camps and Programs':
        desc = SummerCamps.objects.filter(name=name)[0].description
        adr = SummerCamps.objects.filter(name=name)[0].address
    if activity == 'Tutoring':
        desc = Tutoring.objects.filter(name=name)[0].description
        adr = Tutoring.objects.filter(name=name)[0].address
    if activity == 'Youth Employment/Volunteering':
        desc = YouthEmployment.objects.filter(name=name)[0].description
        adr = YouthEmployment.objects.filter(name=name)[0].address


    geolocator = Nominatim(user_agent="convert_to_coords")

    print(adr)

    location = geolocator.geocode(adr)
    # print(adr)
    # print(location)
    # print(location.latitude)
    # print(location.longitude)
    return render(response, 'main/map.html', {'name':name, 'desc':desc, 'adr':adr, 'lat':location.latitude, 'lng':location.longitude})
