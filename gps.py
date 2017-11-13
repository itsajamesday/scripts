import requests
import json
import sys

send_url = 'http://freegeoip.net/json/' + sys.argv[1]
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

l = str(lat)
o = str(lon)
print "Latitude : "+l
print "Longitude:"+o
print "https://www.google.co.uk/maps/@"+l+","+o+",14z?hl=en&authuser=0"
