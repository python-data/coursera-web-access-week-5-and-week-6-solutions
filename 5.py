import urllib
import json
import urllib.request

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location:')
url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})
print ('Retrieving:',url)
html = urllib.request.urlopen(url)
data = html.read()
print ('Retrieved',len(data),'characters')
print(data)

try: js = json.loads(str(data))
except: js = None

if 'status' not in js or js['status'] != 'OK':
    print ('==== Failure To Retrieve ====')
results = js['results']

print (results[0]['place_id'])
