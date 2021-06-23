import requests

from datetime import datetime

api_key = '2547de0af8e84cf1cd49e6217778046a'
location = input("Enter the city name : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

with open("output.txt", "w") as result_file:

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    space = "\n"
    result_file.write(str(location))
    result_file.write(str(space))
    result_file.write(str(temp_city))
    result_file.write(str(space))
    result_file.write(weather_desc)
    result_file.write(str(space))
    result_file.write(str(hmdt))
    result_file.write(str(space))
    result_file.write(str(wind_spd))
    result_file.write(str(space))
    result_file.write(str(date_time))


print("----------------------------------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))
print("-----------------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  : ",weather_desc)
print("Current Humidity      : ",hmdt, '%')
print("Current wind speed    : ",wind_spd, 'kmph')