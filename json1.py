'''javascript object notation '''
import json

with open('states.json') as f:
    data =json.load(f)

for state in data['states']:
    #print state['name'], state['abbreviation']
    del state['area_codes']


with open ('new_states.json','w') as f:
    json.dump(data,f,indent=2,sort_keys)




 
