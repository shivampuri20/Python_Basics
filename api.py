import json
from urllib import urlopen
response= urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
source = response.read()

#print source


data= json.loads(source)
print json.dumps(data,indent=2)

#print len(data['list']['resources'])

for item in data['list']['resources']:
    #print item
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price
    



