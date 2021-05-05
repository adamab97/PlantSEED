import json
#must import json library into python3 in order to use its functions
control_file = open("central_carbon_publications", "r")
#opening the control file that contains the infromation to be added to the json file
control_dict = {}
#assigning an empty variable that will become the dictionarycontaining information to be added to the json file
for line in control_file:
#parsing the control file to find information to add
	stripped_line = line. strip()
	my_list = stripped_line. split('\t')
	#previous two lines convert the information in the "flat", "tab-seperated" control file to a useable format
	control_dict[my_list[0]] = {'publication':my_list[1]}
	#creation of the control dictionary, utilizes the formatting of the flat file to assign the first location in the flat file to a gene and the second its publication
	#must structure flat file in a way that will be useable with the nested dictionary structure of json
control_file. close()
#must close flat file to continue after operations are complete, now have a control dict that encompasses each of the lines in the flat file to be added to json

f = open('../../../../Data/PlantSEED_v3/PlantSEED_Roles.json')
data = json.load(f)
#must load json files this way
for my_entry in data:
#parsing using new variables
	for my_feature in my_entry['features']:
		if(my_feature in control_dict):
		#parsing for genes that are contained within the flat file 
			my_jsonpub = my_entry['publications']
			my_addedpub = control_dict[my_feature]['publication']
			#assigning variables to the locations of interest within the json file
			if my_addedpub not in my_jsonpub:
			#parsing for information specifically contained within control file
				my_jsonpub.append(my_addedpub)
				#command that physically changes the json file

with open ('../../../../Data/PlantSEED_v3/PlantSEED_Roles.json','w') as out_file:
	json.dump (data, out_file, indent=4)
	#way to make the changes appear within the json file with the correct formatting
