import openrouteservice
import json
import folium
from openrouteservice import convert



client = openrouteservice.Client(key='5b3ce3597851110001cf62480449e75063564d28ad2b9bc79cc1d62e')


coords = [[5.7357819,45.1875602],[6.1288847,45.8992348]]
#call API
res = client.directions(coords)
#test our response
with(open('test2.json','+w')) as f:
 f.write(json.dumps(res,indent=4, sort_keys=True))

decoded = convert.decode_polyline(res['routes'][0]['geometry'])

distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
duration_txt = "<h4> <b>Temps :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
