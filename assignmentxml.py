import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_350980.xml'  
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data  
tree = ET.fromstring(data)
counts = tree.findall('.//count')

count = 0
sum = 0
for num in counts:
    #print num 
    int_number = int(num.text)
    count = count + 1
    sum = sum + int_number  
print "Count: ", count
print "Sum", sum       
