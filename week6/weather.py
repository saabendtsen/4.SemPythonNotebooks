import json
import requests

#Create a small program that can get whether data from Aarhus

url = "http://api.openweathermap.org/data/2.5/weather"
query = {'q': 'Aarhus,dk', 
         'mode': 'json',                       
         'units': 'metric',
         'appid': "5e44e3de8ae959f1b8b84e208b50c23b"}
r = requests.get(url, params=query)

print(r.json())