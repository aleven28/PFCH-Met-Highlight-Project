# PFCH-Met-Highlight-Project
Met object record and Wikidata mashup.

The aim of this project was to compare object records from the Metropolitan Museum of Art API with corresponding data from the Wikidata API. The MET data is limited to all of the object records coded as 'isHighlight' in the collection. 

Step 1: methighlightparse.py

Use the requests module to get object ids from the Met API that contain the tag 'isHighlight'(https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=*). Create your own directory (in this case named objects_json)to pull the object records obtained by inserting object ids into objects url (https://collectionapi.metmuseum.org/public/collection/v1/objects/). Save object records into individual JSON files in directory. Optionally, combine the individual files into one big JSON file. 

Step 2: wikidataqids.py

Open up the individual object JSON files using glob. Use a regular expression to create a list of wikidata object ids from the object records (qids.json).

Step 3: wikidataparse.py

Insert qids from qids.json into a SPARQL query to extract 'instanceOf' and 'instanceOfLabel' properties from Wikidata endpoint. Create an empty dictionary and fill with a counter of occurrence of these properties. Save into a separate JSON file called instancecount.json.

Step 4: visualization.py

Separate the instancecount.json data into individual dictionaries to make it more digestible for visualization in Tableau Public. Final JSON file called visualization.json. 

Visualizations:
https://public.tableau.com/views/METHighlightTreemapVisualization/Sheet1?:language=en-GB&:display_count=n&:origin=viz_share_link
https://public.tableau.com/views/METHighlightBubblesVisualization/Sheet1?:language=en-GB&:display_count=n&:origin=viz_share_link


