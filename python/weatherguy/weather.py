import pyowm
from w_logger import newlog, log

newlog()
log('lets go')

import time
sleep_minutes = 20

APIKEY = "9d9eb1b9634e1afd7404c9fbb0e4ce7f"
owm = pyowm.OWM(APIKEY)  # You MUST provide a valid API key

while(True):
    log("time to checkup")
    observation = owm.weather_at_place('Copenhagen,DK')
    w = observation.get_weather()
    w_json = w.to_JSON()
    log(str(w_json))
    print(w_json)
    time.sleep(sleep_minutes * 60)


# from pprint import pprint
# import requests
#
# APIKEY = '{9d9eb1b9634e1afd7404c9fbb0e4ce7f}'
# APIURL = 'http://api.openweathermap.org/data/2.5/weather?q=London&APPID='
#
# print(APIURL+APIKEY)
#
# r = requests.get(APIURL+APIKEY)
# pprint(r.json())


# ----

# # Attempt 3
# import pyowm
#
# APIKEY = "9d9eb1b9634e1afd7404c9fbb0e4ce7f"
# owm = pyowm.OWM(APIKEY)  # You MUST provide a valid API key
#
#
# observation = owm.weather_at_place('Copenhagen,DK')
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
#
# # Weather details
# print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)


# FAILURE 2 - API key problems
# import pyowm
#
# owm = pyowm.OWM('9d9eb1b9634e1afd7404c9fbb0e4ce7f')  # You MUST provide a valid API key
#
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
#
# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('London,GB')
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
#
# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
#


# FAILURE 1 - API key problems

# from pprint import pprint
# import requests
#
# APIKEY = '{9d9eb1b9634e1afd7404c9fbb0e4ce7f}'
# APIURL = 'http://api.openweathermap.org/data/2.5/weather?q=London&APPID='
#
# print(APIURL+APIKEY)
#
# r = requests.get(APIURL+APIKEY)
# pprint(r.json())
