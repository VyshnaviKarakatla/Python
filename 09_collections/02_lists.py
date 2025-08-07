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


#pop()
list_num_pop=[10,20,30,40]
list_num_pop.pop()
print(list_num_pop)
removed_element=list_num_pop.pop()
print(removed_element)
removed_element=list_num_pop.pop(1)
print(removed_element)

#remove()
list_nums_remove=[10,20,30,40,50]
print(list_nums_remove)
list_nums_remove.remove(50)
print(list_nums_remove)

#clear()
list_nums_clear=[10,20,30]
list_nums_clear.clear()
print(list_nums_clear)

#index()
list_nums_index=[10,20,30,40]
print(list_nums_index.index(20))
print(list_nums_index.index(30))

#start and stop
list_nums_start_stop=[10,20,30,40,10,10,20,30,20,10,20]
print(list_nums_start_stop.index(20))
print(list_nums_start_stop.index(20,2)) #start
print(list_nums_start_stop.index(20,4,8)) #start and stop

#count()
list_nums_count=[10,20,30,40,10,10,20,30,20,10,20]
print(list_nums_count.count(20))

#reverse()
list_nums_reverse=[10,20,30,40,50]
print(list_nums[::-1])

#sort()
list_nums_sort=[30,10,40,60,20]
list_nums_sort.sort()
print(list_nums_sort)
list_nums_sort.sort(reverse=True)
print(list_nums_sort)

#copy()
list_nums_copy=[10,20,30,40,50,60]
bk_list=list_nums_copy.copy()
print(bk_list)