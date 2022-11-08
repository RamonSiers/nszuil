import requests
import json

api_key = "9db0e8ba7a426ccc993e2cd352675c65"
lat = "52.1092717"
lon = "5.1809676"
url = "http://api.openweathermap.org/data/2.5/weather?appid=9db0e8ba7a426ccc993e2cd352675c65&q=Utrecht&units=metric&lang=nl"

response = requests.get(url)
data = json.loads(response.text)
print(data)

print("De Temperatuur is",data["main"]["temp"],"graden")
print(" Het is",data["weather"]["description"])



# id = x['criteria'][0]['id']