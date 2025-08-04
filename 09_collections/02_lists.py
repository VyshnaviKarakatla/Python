#lists
#empty list
empty_list=[]
print(type(empty_list))
print(empty_list)

#list with nums
list_nums=[10,20,30]
print(list_nums)

#list with text
list_text=["python", "java", "cloud"]
print(list_text)

#list with nums and text
list_nums_and_text=[10,20,30,"python", "java"]
print(list_nums_and_text)

#list inside list
list_in_list=[10,20,[30,40,50]]
print(list_in_list)

#using class list
#class_list=list(10,20,30)-TypeError
class_list=list([10,20,30])
print(class_list)

#Accessing elements in list
list=[10,20,30,40,50]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[:])
print(list[1:4:1])
print(list[1::])
print(list[::-1])

#Memoryaddress
num1=10
num2=10
print(id(num1))
print(id(num2))
list1=[10,20,30]
list2=[10,20,30]
print(id(list1))
print(id(list2))

#loops in list
list_loop=[10,20,30,40,50]
for i in list_loop:
    print(i)

#using range
range_list=(range(0,26,5))
print(range_list)

custom_list=(range(0,26,5))
for i in custom_list:
    print(i*2)

#perform conditinals
days=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
day=input("Enter a day in week: ")
if day in days:
    print("Day exists")
else:
    print("Invalid day")

#append()
list_num_append=[10,20,30]
#list_num_append.append(40,50)-TypeError
list_num_append.append([40,50])
print(list_num_append)
list_num_append.append("hello")
print(list_num_append)

#extend()
list_num_extend=[10,20,30,40]
#list_num_extend.extend(50)-TypeError
list_num_extend.extend([50])
print(list_num_extend)
list_num_extend.extend([50,60])
print(list_num_extend)
list_num_extend.extend("hello")
print(list_num_extend)

#insert()
list_num_insert=[10,20,30,40,50]
list_num_insert.insert(1,100)
print(list_num_insert)
list_num_insert.insert(10,"hi")
print(list_num_insert)
list_num_insert.insert(10,10000)
print(list_num_insert)
