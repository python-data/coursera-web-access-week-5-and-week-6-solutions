import urllib
import xml.etree.ElementTree as ET
import urllib.request
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    print ('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    #lst = tree.findall('.//count')
    print ('Count: ', len(lst))
    num = 0
    for item in lst:
        x = item.find('count').text
        num = num + int(x)
    print ('Sum: ', num)
