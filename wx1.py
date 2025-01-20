#! /usr/bin/python3

# import required modules
import requests, json, sys, os
from latlon2maiden import maidenhead2latlon

# Get Open Weather Map API key 
RCFILE=os.path.expanduser("~/.keyerrc")
with open(RCFILE) as f:
    SETTINGS = json.load(f)
print(SETTINGS)
api_key = SETTINGS['MY_OWM_API_KEY']

#city = input('Enter city name: ')
city='syracuse,ny,us'
city='ramona,ca,us'
#lat=32.96
#lon=-116.833
zipcode=92065

MY_GRID = SETTINGS['MY_GRID']
lat, lon = maidenhead2latlon(MY_GRID)
print('lat='lat,'\tlon=',lon)

if 1:

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    #url = f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={api_key}'

    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()
        print(data)
        temp_k = data['main']['temp']
        temp_c = temp_k-273
        temp_f = temp_c*9/5+32
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp_k} K = {int(temp_c)} C = {int(temp_f)} F')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')

else:

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #base_url = "http://api.openweathermap.org/data/3.0/weather?"
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    print('x=',x)
    print('cod=',x["cod"])
    
    if x["cod"] == "401":
        print('msg=',x["message"])
        sys.exit(0)
        
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        
        # store the value of "main"
        # key in variable y
        y = x["main"]
        
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
        
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
        
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
        
        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z
        weather_description = z[0]["description"]
        
        # print following values
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n description = " +
              str(weather_description))
        
    else:
        print(" City Not Found ")
        
