import re, json
translation = {}

# https://esoitem.uesp.net/dumpMinedItems.php?type=29&output=csv


with open('Furnishings.csv') as fil:
	data = fil.read()
	'''
	data = data.split("\n")


	for rows in range(len(data)):
		if "INGREDIENTS" in data[rows]:
			print(data[rows+1])

	#print(data)
	'''
	output = list(re.findall(r'","(.*?)",".*?","INGREDIENTS\n(.*?)\n', data))
	for x in output:
		name = re.sub(r'(.*?: )','',x[0])
		ingredients = x[1].split(", ")
		#print("")
		curIngred = {}
		for y in ingredients:
			counts = re.findall(r'.*? \((.*?)\)', y)
			if len(counts) == 0:
				count = 1
				nameI = y
			else:
				count = int(counts[0])
				nameI = re.sub(r' \((.*?)\)','', y)

			curIngred[nameI]=count

		#print(curIngred)
		translation[name] = curIngred
		'''
		print(name)
		print(ingredients)
		print("")
		'''
fil.close()


#print(translation)

'''
while True:
	Search = input("What to search for: ")
	try:
		ingredients = translation[Search]
		print("Ingredients Required")
		for x in ingredients:
			print(f'{x[1]} x {x[0]}')
		print("")
	except KeyError:
		print("Did not find the search term.")
'''
fil = open('furnishings.json','w')
#print(json.dumps(translation))
json.dump(translation, fil)
fil.close()
fil = open('fakeFurnishingsJSON.js','w')
fil.write(f'var translation = {json.dumps(translation)}')
fil.close()
