import json
import requests


url = "https://query.wikidata.org/sparql"

qnumbers = json.load(open('qids.json'))


sparql = """

SELECT ?item ?itemLabel ?instanceOf ?instanceOfLabel
        WHERE 
           {
          
        VALUES ?item {<REPLACEME>}
		optional{
	?item wdt:P31 ?instanceOf
	    }
	 SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }

	}
		"""

# Insert Met object record QIds into Sparql query:

edited_qs =[]

for q in qnumbers:
    edited_qs.append(f"wd:{q}")

replace_string = " ".join(edited_qs)

sparql = sparql.replace('<REPLACEME>',replace_string)


params = {
	'query' : sparql
    }

headers = {
	'Accept' : 'application/json',
	'User-Agent': 'USER  - MET highlight project ' #Create your own User-Agent. 
}

r = requests.post(url, data=params, headers=headers)

data = json.loads(r.text)
			
		

instancecount = {}

for result in data['results']['bindings']:
	if 'instanceOfLabel' in result:
		if result['instanceOfLabel']['value'] not in instancecount:
			
			instancecount[result['instanceOfLabel']['value']] = 0

		instancecount[result['instanceOfLabel']['value']]+=1

with open('instancecount.json', 'w') as out: 
    json.dump(instancecount,out, indent=2)
















   