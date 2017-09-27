import urllib
import json
import urllib.request

url =input("Enter json URL: ")
connection = urllib.request.urlopen(url)
raw_data = connection.read()
parsed_data = json.loads(raw_data)
counts = []

comments = parsed_data["comments"]

for comment in comments:
    counts.append(comment['count'])

print( "Sum: {0}".format(sum(counts)))
