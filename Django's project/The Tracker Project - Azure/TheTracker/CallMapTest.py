# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("New Hampshire United States")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)