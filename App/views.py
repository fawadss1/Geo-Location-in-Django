from django.shortcuts import render
from django.contrib import messages
import requests
import json

# Create your views here.
def index(request):
    try:
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get(f'http://ip-api.com/json/{ip_data["ip"]}')
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        return render(request, 'index.html', {'data': location_data})
    except:
        messages.error(request, 'Error Occured While Retrieving Data')
        return render(request, 'index.html')

