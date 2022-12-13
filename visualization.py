import json
import requests 

instancecount = json.load(open('instancecount.json'))

count = []

for item in instancecount:

	editdict = { 
	'instance of' : item,
	'count' : instancecount[item]}
	count.append(editdict)

	print(editdict)

with open('visualization.json', 'w') as out: 
    json.dump(count,out, indent=2)

    