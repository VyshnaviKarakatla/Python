import json
student={
    'id':101,
    'name':'ravi',
    'couse':'Python Full Stack',
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

#creating and writing json file
with open('students_data.json','w') as file:
    json.dump(student,file,indent=4)

#reading json file
with open('students_data.json','r') as file:
    json_read=json.load(file)
    print(json_read)
    print(json_read['name'])
    print(json_read['skills'][0])


#Operations b/w string and json
#convert json to string
json_to_string=json.dumps(student)
print(json_to_string)
print(type(json_to_string))

#convert string to json
string_to_json_string='{"id": 101, "name": "ravi", "couse": "Python Full Stack"}'
string_to_json=json.loads(string_to_json_string)
print(string_to_json)
print(type(string_to_json))