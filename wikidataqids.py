import json
import glob
import re

#Regular expression for extracting object Wikidata Ids.

wikidataqids = []

for highlight in glob.glob('objects_json/*.json'):
    with open(highlight) as jsonfile:

        data = json.load(jsonfile)
    
        if 'objectWikidata_URL' in data:
            if data['objectWikidata_URL'] != '':

                qidsearch = data['objectWikidata_URL']
                text = qidsearch
                pattern = re.compile(r'Q[0-9]*')
                results = pattern.search(text)

                wikidataqids.append(results.group())


                with open('qids.json' , 'w') as out:
                    json.dump(wikidataqids, out)
