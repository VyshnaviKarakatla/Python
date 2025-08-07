#tuples
#empty tuple
empty_tuple=[]
print(type(empty_tuple))
print(empty_tuple)

#tuple with nums
tuple_nums=(10,20,30)
print(tuple_nums)

#tuple with text
tuple_text=("python", "java", "cloud")
print(tuple_text)

#tuple with nums and text
tuple_nums_and_text=(10,20,30,"python", "java")
print(tuple_nums_and_text)

#tuple inside list
tuple_in_tuple=(10,20,(30,40,50))
print(tuple_in_tuple)

#using class tuple
#class_tuple=tuple(10,20,30)-TypeError
class_tuple=tuple((10,20,30))
print(class_tuple)

#Accessing elements in list
tuple=(10,20,30,40,50)
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
print(tuple[:])
print(tuple[1:4:1])
print(tuple[1::])
print(tuple[::-1])

#loops in tuple
tuple_loop=(10,20,30,40,50)
for i in tuple_loop:
    print(i)

#using range
range_tuple=(range(0,26,5))
print(range_tuple)

custom_tuple=(range(0,26,5))
for i in custom_tuple:
    print(i*2)

#perform conditinals
days=("sunday","monday","tuesday","wednesday","thrusday","friday","saturday")
day=input("Enter a day in week: ")
if day in days:
    print("Day exists")
else:
    print("Invalid day")

#Tuples are immutable so only index() and count() are allowed
#index()
tuples_nums_index=[10,20,30,40]
print(tuples_nums_index.index(20))
print(tuples_nums_index.index(30))

#count()
tuple_nums_count=[10,20,30,40,10,10,20,30,20,10,20]
print(tuple_nums_count.count(20))

#packing and unpacking
person=("john", 25,"Python") #packing
name,age,course=person   #unpacking
print(name)
print(age)
print(course)

t1=([10,20], [30,40], [50,60])
print(t1[0][0])
t1[0][0]=100 #modifying list inside tuple
print(t1)