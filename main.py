import requests
import os
from pprint import pprint
#Import lib .env file
from dotenv import load_dotenv

load_dotenv()  # load .env file into environment variables (if it exists)

API_KEY = os.getenv("API_KEY")

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data )