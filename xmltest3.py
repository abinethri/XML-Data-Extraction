import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET.fromstring(input)

# findsall id tags under user and makes a list 

# or use lst = stuff.findall('.//user/id')
# or lst = stuff.findall('.//user[@x]/id')
lst = stuff.findall('.//user/id')

#iterates through id tags and gets the text 
for item in lst:
    print 'Id:', item.text 
    
    
