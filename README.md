# PFCH-Met-Highlight-Project
Met object record and Wikidata mashup.

The aim of this project was to compare data from the Metropolitan Museum of Art API with corresponding data from the Wikidata API. The MET data is limited to all of the object records coded as 'isHighlight' in the collection. 

Step 1: methighlightparse.py

Use the requests module to get object ids from the Met API that contain the tag 'isHighlight'(https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=*). Create your own directory (in this case named objects_json)to save the object records obtained by inserting object ids into objects url (https://collectionapi.metmuseum.org/public/collection/v1/objects/).


