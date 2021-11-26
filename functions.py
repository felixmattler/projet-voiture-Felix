import folium
import openrouteservice
from geopy.geocoders import Nominatim
from openrouteservice import convert
import requests
import json


API_URL = "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region"

def get_geo_parameter(depart,arrive):

	geolocator = Nominatim(user_agent="Pierre")
	location = geolocator.geocode(depart)
	depart = [location.longitude,location.latitude]
	location = geolocator.geocode(arrive)
	arrive = [location.longitude,location.latitude]
	center = [(arrive[1]+depart[1])/2,(depart[0]+arrive[0])/2]

	return [depart,arrive]


def coords_calc(coords):

	client = openrouteservice.Client(key='5b3ce3597851110001cf62480449e75063564d28ad2b9bc79cc1d62e')
	
	res = client.directions(coords)
	
	return res


def make_map_great_again(res,coords):

	center = [(coords[0][1]+coords[1][1])/2,(coords[0][0]+coords[1][0])/2]
	decoded = convert.decode_polyline(res['routes'][0]['geometry'])
	distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
	m = folium.Map(location=center,zoom_start=7, control_scale=True,tiles="cartodbpositron")
	folium.GeoJson(decoded).add_child(folium.Popup(distance_txt,max_width=300)).add_to(m)
	folium.Marker(
	    location=list(coords[0][::-1]),
	    popup="Grenoble",
	    icon=folium.Icon(color="blue"),
	).add_to(m)

	folium.Marker(
	    location=list(coords[1][::-1]),
	    popup="Annecy",
	    icon=folium.Icon(color="green"),
	).add_to(m)

	return m


def add_markers(m,stop_points):

	i = 1

	for stop_point in stop_points:


		folium.Marker(
		    location=list(stop_point[::-1]),
		    popup="Arrêt " + str(i),
		    icon=folium.Icon(color="red"),
		).add_to(m)

		i=i+1

	return m




def get_segment(depart, arrive, autonomie):

	stop_points = []
	point_special = [abs(depart[0]-arrive[0]),abs(depart[1]-arrive[1])]
	segment=[abs(point_special[1]/autonomie),abs(point_special[0]/autonomie)]

	for i in range(1,int(autonomie)):

		stop_point = []

		if depart[0]>arrive[0]:
			stop_point.append(round(depart[0] - (segment[1]*i),6))

		else :
			stop_point.append(round(depart[0] + (segment[1]*i),6))
			

		if depart[1]>arrive[1]:
			stop_point.append(round(depart[1] - (segment[0]*i),6))

		else :
			stop_point.append(round(depart[1] + (segment[0]*i),6))

		stop_points.append(stop_point)


	# print(stop_points)

	return stop_points


def request_api(coord):

	rayon = 60000
	URL = API_URL+"&geofilter.distance="+str(coord[1])+"%2C"+str(coord[0])+"%2C"+str(rayon)
	
	response=requests.get(URL)
	content = json.loads(response.content.decode("utf-8"))

	borne = content['records'][0]['geometry']['coordinates']
	ville = content['records'][0]['fields']['ad_station']
	return borne


request_api([6.129384,45.899247])

#test our response
