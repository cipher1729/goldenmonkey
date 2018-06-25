#assume latitude longitude as input

# importing the requests library
import requests
import json

# location given here
location = "47.673988, -122.121513" 
radius=1500
types=['convenience_store', 'department_store','gas_station','liquor_store', 'shopping_mall', 'supermarket', 'store']
placesURL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params={}
params['location']= location
params['radius']= radius
params['key']= "AIzaSyBBSXOW-4UoDd7ionv-gDaDBwobfR4OFys"

f= open('nearby_places.txt','w')
 

def genPlaces():
		for type in types:
			params['type']= type
			# sending get request and saving the response as response object
			r = requests.get(url = placesURL, params = params)
 
			# extracting data in json format
			data = r.json()

			f.write( json.dumps(data, indent=4, sort_keys=True))

genPlaces()
 
 
# extracting latitude, longitude and formatted address 
# of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']
 
# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      %(latitude, longitude,formatted_address))
