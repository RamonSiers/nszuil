import requests
import json
import time

resource_uri = "https://weerlive.nl/api/json-data-10min.php?key=d23be7ec47&locatie=Utrecht"
params = {
    "temp": '',
    "samenv":''
}


response = requests.get(resource_uri)
response_data = response.json()

temp = ''
samenv = ''
location = "De Bilt"


url = "https://weerlive.nl/api/json-data-10min.php?key=d23be7ec47&locatie=De Bilt"
response = requests.get(url)
data = response.json()
""" Below are all available keys, simply select the ones you want.
keyList = [
	'temp','samenv']
"""
keyList = [
	temp,samenv
]

weerDict = {}
print("Getting data for " + location)
for weer in data['liveweer']:
	print("Adding all fields as string first:", end = '')
	for key in keyList:
		try:
			weerDict[key] = weer.get(key)
			print(" " + str(key), end = '')
		except:
			print("", end = '')
	print("\n\nThese look numbery, re-adding as float:", end = '')
	for key in keyList:
		try:
			weerDict[key] = float(weer.get(key))
			print(" " + str(key), end = '')
		except:
			print("", end = '')
""" InfluxDB needs UTC data, the source has no timstamp, so create one. """
weerliveData = [
	{
	"measurement":"WeerliveData",
	"tags":
		{
			"Location": location
		},
	"fields": weerDict
	}
	]

print(temp)
print(samenv)
