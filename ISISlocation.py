import requests


# get the sunrise and sunset data for your location

parameter = {
    "lat": 27.489971,
    "lng": 77.681738
}


res = requests.get("https://api.sunrise-sunset.org/json", params=parameter)

print(res.json())
print(res.raise_for_status())


