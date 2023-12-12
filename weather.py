from pprint import pprint
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_current_weather(city):
  request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=67943f961ac4423f7352d3c25d6bfee2&units=metric'
  weather_data = requests.get(request_url).json()
  return weather_data

if __name__ == '__main__':
  print('\n***Get Weather conditions***\n')
  city = input('Please enter a city name: ')

  # check for empty strings or string with only spaces
  if not bool(city.strip()):
    city = "ChangSha"
    
  weather_data = get_current_weather(city)
  
  print('\n')
  pprint(weather_data)