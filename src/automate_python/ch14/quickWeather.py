
# quickWeather.py - Prints the weather for location from the commad line

import json
import requests
import sys
import collections.abc

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/forecast/daily' + \
    '?q=%s&cnt=3&appid=274ba5227b4dd0c008ffbf8eca859037' % (location)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
