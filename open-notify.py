#Function to find current ISS location and number of astronauts in realtime
#Using Open Notify API to get the ISS data

import requests, reverse_geocode

loc_response = requests.get("http://api.open-notify.org/iss-now.json")
coordinates_data = loc_response.json()
coordinates = (coordinates_data['iss_position']['latitude']),(coordinates_data['iss_position']['longitude'])
location = reverse_geocode.get(coordinates)

astro_response = requests.get("http://api.open-notify.org/astros.json")
astro_data = astro_response.json()

# 9 people are currently in space.
# print astro_data['number']
print "Current ISS location is "+ location['city'] +", "+location['country']
print "There are " + str(astro_data['number']) +" astronauts in ISS right now: " 
for i in range(0,astro_data["number"]):
	print "Name: "+ astro_data['people'][i]['name'] + ", Craft: " + astro_data['people'][i]['craft']