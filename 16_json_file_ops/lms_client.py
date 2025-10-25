#Filetering users whose age is less than 30 from json file
import json
with open('lms.json','r') as file_data:
    data=json.load(file_data)
    print('Nummber of users: ', len(data['users']))
    for user in data['users']:
        if user['age']<30:
            print(user['username'],user['age'])