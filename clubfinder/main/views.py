from django.shortcuts import render
from django.http.response import HttpResponse
import requests, json
import os

def index(response):
    return render(response, 'main/index.html', {})