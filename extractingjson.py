import urllib.request as ur
import json

data_url = "http://py4e-data.dr-chuck.net/comments_489977.json"

#Reading the URL and parsing its data
urldata = ur.urlopen(data_url).read()
data = json.loads(urldata)

#Finding each "count" field and adding its value to the total sum.
total = 0
for comment in data["comments"]:
	total += comment["count"]

print("TOTAL SUM: ", total)
