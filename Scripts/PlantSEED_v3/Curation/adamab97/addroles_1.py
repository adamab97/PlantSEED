import json
#must import json library into python3 in order to use its functions
control_file = open("choline_biosynth_loc_2", "r")
#opening the control file that contains the infromation to be added to the json file
control_dict = {}
#assigning an empty variable that will become the dictionarycontaining information to be added to the json file
for line in control_file:
#parsing the control file to find information to add
	stripped_line = line. strip()
	my_list = stripped_line. split('\t')
	#previous two lines convert the information in the "flat", "tab-seperated" control file to a useable format
	control_dict[my_list[1]]={'role':my_list[0],'localization':my_list[2],'source':my_list[3]}

control_file. close()
#must close flat file to continue once operations on it are complete, now have a control dict that encompasses each of the lines in the flat file to be added to json

f = open('../../../../Data/PlantSEED_v3/PlantSEED_Roles.json')
data = json.load(f)
#must load json files this way
for my_entry in data:
	#parsing using new variables data== json imported data
	for my_feature in my_entry['features']:
	#parsing for arbitrary variable value within the features key in the json file
		if(my_feature in control_dict and control_dict[my_feature]['role'] == my_entry['role']):
		#parsing for assigned variable further within the control file to find matches and further isolate desired data
			my_location = control_dict[my_feature]['localization']
			#assigning another variable
			if(my_location in my_entry['localization']):
			#further parsing, essentially disgarding any information that doesnot fit out parameters
				print("Location already there: "+my_location)
				#first action within else statement 
			else:
				print("Location not there: "+my_location)
				#seconf action in else statement accounts for if information is not already in the desired location within the json
				my_entry['localization'][my_location] = {my_feature: [ control_dict[my_feature]['source'] ]}
				#assignment of the control file information once the else statement is triggered
			for entry_location in my_entry['localization']:
				print(my_entry['localization'][entry_location], entry_location, my_entry['role'])
				#check to see if it workedß
with open('../../../../Data/PlantSEED_v3/PlantSEED_Roles.json', 'w') as out_file:
	json.dump (data, out_file, indent=4)
	#way to make the changes appear within the json file with the correct formatting
