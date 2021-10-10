##################################################################################################
#Purpose: The program will prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, compute the sum of the numbers 
# in the file.
# Look through all the <comment> tags and find the <count> values then sum the numbers

##################################################################################################

# importing the libraries
from urllib.request import urlopen
import xml.etree.ElementTree as ET #Importing library.
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1277929.xml'
data= urlopen(url, context=ctx).read()  # Open URL and read the raw HTML content
#print(data)
tree = ET.fromstring(data) #Read the string from 
lst = tree.findall('.//count') #Find all comment tag that is child of comments and return a list of tags
#print(lst)
#print('Comment Count:', len(lst))

sum = 0
for item in lst:#Iterate through the tags that are children of comments
    sum = sum + int(item.text)
print(sum)
  