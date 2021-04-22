import re
import json

translation = {}
prices = {}

fil = open("PriceTable.lua")
text = fil.read()
fil.close()
outputsL = re.findall(r'\[([0-9]*?)\]={\[[0-5]]={\[[0-9]*?\]={\[-1\]={.*?"Avg"]=(.*?),',text)

fil = open("ItemLookUpTable_EN.lua")
text = fil.read()
fil.close()
translationL = re.findall(r'\["(.*?)"\]={\[[0-9]*?]=(.[0-9]*?),}', text)
for x in translationL:
	translation[x[1]] = x[0]

for x in outputsL:
	try:
		prices[translation[x[0]]] = x[1]
	except KeyError:
		print(f"Item {x} not found")

fil = open("prices.json",'w')
json.dump(prices, fil)
fil.close()
'''
fil = open('pricesJSON.js','w')
fil.write(f'var prices = {json.dumps(translation)}')
fil.close()
'''