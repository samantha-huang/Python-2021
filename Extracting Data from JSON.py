#json.load() takes a file object and returns the json object. 
# A JSON object contains data in the form of key/value pair. 
# The keys are strings and the values are the JSON types. 
# Keys and values are separated by a colon. Each entry (key/value pair) is separated by a comma.

# importing the libraries
from urllib.request import urlopen
import json #import json library
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1277930.json'
data= urlopen(url) # Open URL 
info = json.load(data) # returns JSON object as a dictionary
#print(info)

sum = 0
for i in info["comments"]:
    ct = i['count']
    #print(ct)
    sum = sum + ct
print(sum)

