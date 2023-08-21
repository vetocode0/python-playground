import requests

city = 'Atlanta'
url = 'http://api.weatherapi.com/v1/current.json?key=dc0efdfb91c7431483734142230808&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

location = weather_json.get('location').get('name')
temperature = weather_json.get('current').get('temp_f')
condition = weather_json.get('current').get('condition').get('text')

print("The current temperature in ", location, " is ", temperature, " and the weather is ", condition, ". Enjoy your day!", sep='')