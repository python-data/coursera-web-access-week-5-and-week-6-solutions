import urllib
import ssl
from bs4 import BeautifulSoup
import urllib.request
url = input('Enter URL : ')
position = input('Enter position : ')
count = input('Enter count : ')

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.request.urlopen(url, context=scontext)
data = uh.read()
soup = BeautifulSoup(data)

# Retrieve all of the anchor tags
tags = soup('a')

links = list()

for tag in tags:
    links.append(tag.get('href', None))

print ('Retrieving: ', links[0])
print ('Retrieving: ', links[int(position)-1])

link = links[int(position)-1]
counter = 1
while counter < int(count):
    uh = urllib.request.urlopen(link, context=scontext)
    data = uh.read()
    soup = BeautifulSoup(data)

    # Retrieve all of the anchor tags
    tags = soup('a')

    links = list()

    for tag in tags:
        links.append(tag.get('href', None))
    print ('Retrieving: ', links[int(position)-1])
    link = links[int(position)-1]
    counter = counter + 1
