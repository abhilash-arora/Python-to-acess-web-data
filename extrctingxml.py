import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
count=0
sum=0
for i in lst:
    x = int(i.find('count').text)
    count =count+1
    sum = sum+x

print("Count : ",count)
print("Sum : ",sum)
