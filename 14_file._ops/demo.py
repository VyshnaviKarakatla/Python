#creating file and writing in file
with open('data.txt','w') as file:
    file.write('Welocome to Python')
    print(file)

with open('data.txt','w') as file:
    file.writelines(['Welocome to Python\n','Welocome to Java\n','Welocome to Git\n'])
    print(file)

#reading file
with open('data.txt','r') as file:
    print(file.read())

with open('data.txt','r') as file:
    print(file.readlines())

with open('data.txt','r') as file:
    for ch in file.read():
        print(ch)

#append file
with open('text.txt','a') as file:
    file.write('Welocome to Python\n')
    file.write('Welocome to Java\n')
    file.write('Welocome to Git\n')
    file.write('Welocome to Cloud\n')
    print(file)

#delete file
import os
os.remove("text.txt")