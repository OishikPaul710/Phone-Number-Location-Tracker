import phonenumbers
import opencage
import folium

#to extact country name
from phonenumbers import geocoder
num="+919855272829"
pepnum=phonenumbers.parse(num)
country_num=geocoder.description_for_number(pepnum, "en")
print(country_num)

#to display service provider
from phonenumbers import carrier
serviceProv_num=phonenumbers.parse(num)
print(carrier.name_for_number(serviceProv_num,"en"))

from opencage.geocoder import OpenCageGeocode

key='6802cbefb7e14c5b89d1edfd8b58c065'
geocoder= OpenCageGeocode(key)
query=str(country_num)
results=geocoder.geocode(query)
#print(results)

lat= results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
 
print(lat,lng)

#we use folium for connceting map
myMap=folium.Map(location=[lat,lng],zoom_start=500)
folium.Marker([lat,lng],popup=country_num).add_to(myMap)

myMap.save("mylocation.html")
 