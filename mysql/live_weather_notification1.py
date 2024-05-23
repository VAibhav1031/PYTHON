import datetime as dt
import requests

BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
API_KEY="d9d896ce1f5660d091f1f63227d87811"
CITY='Faridabad'

url=BASE_URL+"appid="+API_KEY+'&q='+CITY

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

response=requests.get(url).json()

temp_kelvin=response['main']['temp']
temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humididity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
wind_speed=response['wind']['speed']


import os

def display_notification(title, message):
    system = os.name
    if system == 'nt':  # Windows
        os.system('powershell -Command "New-BurntToastNotification -Text \'{}\' -Title \'{}\'"'.format(title, message))
    elif system == 'posix':  # Linux/Mac
        os.system('notify-send "{}" "{}"  '.format(title,message))


display_notification( "Weather Forecast in",f"{CITY} \n Description : {description}\n Temperature {temp_celsius:.2f} °C \n Feels-Like : {feels_like_celsius:.2f} °C \n Humidity:{humididity}%\n  Wind-Speed : {wind_speed} m/s")

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feeels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humididity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General weather in {CITY}:{description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun rises in {CITY} at {sunset_time} local time")
