import requests
import json
import csv


API_KEY = 'YOUR_KEY'
URL = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001'
payload = {'Authorization': API_KEY}

resp = requests.get(URL, params=payload).json()
locations = resp['records']['location']
weathers = []
for location in locations:
    weather = {}
    weather['locationName'] = location['locationName']
    weather['obsTime'] = location['time']['obsTime']
    weather['TEMP'] = location['weatherElement'][3]['elementValue']
    weather['HUMD'] = location['weatherElement'][4]['elementValue']
    weathers.append(weather)

with open('weathers.csv', 'w', newline='') as csvfile:
    fieldnames = ['locationName', 'obsTime', 'TEMP', 'HUMD']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for weather in weathers:
        writer.writerow({'locationName': weather['locationName'], 'obsTime': weather['obsTime'], 'TEMP': weather['TEMP'], 'HUMD': weather['HUMD']})
