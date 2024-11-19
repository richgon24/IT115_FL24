#
import json

#
data1 = {

    'name':'Rich Gonzalez',
    'age':25,
    'city': 'Long Beach, CA',
    'interests':['Music','Photography','Art','Football','Nature'],
    'is_student': True

}

with open('data1.json','w') as json_file:
    #Dump the Data Dictionary into the JSON file.
    json.dump(data1,json_file,indent=4)

print("You have successfully written to data1.json")


with open('data1.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data1.json")
print(loaded_data)

#########
#Change the content of the JSON Dictionary.

loaded_data['age'] = 11
loaded_data['interests'].append('Videography')


#Resave the altered JSON file.
with open('data1.json','w') as json_file:
    #Dump the Data Dictionary into the JSON file.
    json.dump(data1,json_file,indent=4)

print("You have successfully re-written to data1.json")
