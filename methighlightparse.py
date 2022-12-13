import requests
import json 
import os
import glob


#Pull object Ids and loop through for object records.

departmenturl = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=*"


r = requests.get(departmenturl) 
data = json.loads(r.text)

#Create a directory named objects_json or a directory of your choice.

if not os.path.exists('objects_json/'):
		os.makedirs('objects_json/') 

for object_id in data["objectIDs"]:
    
    if os.path.exists(f'objects_json/{object_id}.json'):
         print('Skipping',object_id)
    else:
         print('Downloading',object_id)
         
    r2 = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}")
    
    data2 = json.loads(r2.text)

    with open(f'objects_json/{object_id}.json', 'w') as out: 
        json.dump(data2,out, indent=2)

objectdata = []
for json_file in glob.glob('objects_json/*.json'):
       data3 = json.load(open(json_file))
       objectdata.append(data3)

json.dump(objectdata, open('methighlight.json','w'),indent=2)

  #For counter:  
		    
          #if r.status_code == 200:
            #counter = counter +1
            #print(counter, ':' , data2['objectID'])
            

     
     
    