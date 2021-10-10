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
# print(type(info)) 
#json.load(file_object) json library method to takes a file object and returns the json object.
#Argument : It takes file object as a parameter. Return : It return json object.
#the file is parsed using json.load() method which gives us a dictionary named data.
sum = 0
for i in info["comments"]:
    ct = i['count']
    #print(ct)
    sum = sum + ct
print(sum)

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

###Yiu need access them with the dictionary_name["key"] syntax to get their values
###Because the count item is also an array of dictionaries, you'll need a nested loop to 
###access all of the items (unless you know you'll always have only one of these; then you could
### access it with a position identifier of [0] instead).




##### Code example below
# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

