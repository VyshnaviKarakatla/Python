#Variables
#Storing variables
student_name='Ram'#string
print(type(student_name)) 
student_age=20 #int
print(type(student_age))
student_gpa=8.5 #float
print(type(student_gpa))

#String concatenation
a="Python"
b=" is"
c=" awesome"
print(a+b+c)

#Memory address
a=20
b=20
print(id(a))
print(id(b))  
# Both a and b point to the same memory address since they have the same value
x=[1,2]
y=[1,2]
print(id(x))
print(id(y))
# Both a and b point to the different memory address since lists are mutable and have different identities

#Other ways 
x=y=z=20
print(x)
print(y)
print(z)

x,y,z=10,20,30
print(x)
print(y)
print(z)

#x,y,z=10,20,30,40
# This will raise an error because there are too many values to unpack
#print(x)
#print(y)
#print(z)

#x='Good'
#y=5
#print(x+y)
# This will raise an error because you cannot concatenate a string and an integer

x='Good'
y=5
print(x,y)

#Concatenation and Interpolation
#Concatenation-> combining strings
#Interpolation-> inserting variables into strings
name='Ram'
age=20
#print('My name is ' + name + ' and I am ' +age+ ' years old.')
# This will raise an error because age is an integer, not a string
print(f'My name is {name} and I am {age} years old.')  
