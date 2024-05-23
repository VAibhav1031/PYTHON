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

temp_kevlvin=response['main']['temp']
temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kevlvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humididity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=response['sys']['sunrise']

import os
import win10toast  # Install using pip: pip install win10toast

def display_notification(title, message):
  system = os.name  # Check OS inside the function
  if system == 'nt':
    toast = win10toast.ToastNotifier()
    toast.show_toast(title, message, icon_path="path/to/your/icon.ico")  # Optional icon
  else:
    os.system('notify-send "{}" "{}" '.format(title, message))


display_notification("Title", f"Temperature(K): {temp_kevlvin}\n Temperature(C) {temp_celsius}\n Feels-Like: {feels_like_celsius}\n Humidity:{humididity}\n Description : {description}")



print(response)