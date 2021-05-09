import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# using urllib, pulls from api of astronauts currently on iss
url = "http://api.open-notify.org/astros.json"

# assign urlopen method to response variable, using defined url to open api
response = urllib.request.urlopen(url)

# use json module to read the response
result = json.loads(response.read())

# create a writable text file named 'iss'
file = open("iss.txt", "w")

# what to write in the file
file.write("There are currently " +
           str(result["number"]) + " astronauts on the ISS: \n\n")

# converts number index pulled from result into a string
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# print longitude and latitude for my IP address/location
g = geocoder.ip('me')
file.write("\n Your current lat/long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# set up the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90) # creates the x and y coordinates of 4 corners of the canvas

# loads the world map image, has to be gif format
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")

# 45 degree angle path when moving
iss.setheading(45)
iss.penup()

# the image opened then immediately closed so I'm adding this func to keep it open
# input('stop')

while True:

    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # extracts the ISS location
    location = result["iss_position"]
    lat = location['latitude'] # pulls this from the index in the API
    lon = location['longitude']

    # Output lat and lon to terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Updates the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 sec
    time.sleep(5)
