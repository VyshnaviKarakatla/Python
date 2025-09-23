#dictionaries
#empty dictionary
empty_dict={}
print(type(empty_dict))
print(empty_dict)

#dictionary with nums
num_dict={1:10,2:20,3:30}
print(num_dict)
print(num_dict[3])

#dictionary with text
text_dict={'course1':'Java','course2':'Python','course3':'cloud'}
print(text_dict)
print(text_dict['course1'])

#mixed text
mixed_dict={1:10,'course1':'Python'}
print(mixed_dict)
print(mixed_dict[1])

#dict inside dic
students={101:{'name':'Ravi','age':20},102:{'name':'krishna','age':20}}
print(students)
print(students[101])

#dict with list and tuple
dict_list_tuple={101:['java','python'],102:('html','css')}
print(dict_list_tuple)
print(dict_list_tuple[101])
print(dict_list_tuple[102])

#update data
fruits={'a':'apple','b':'banana'}
print(fruits)
fruits['c']='cherry'
print(fruits)

fruits={'a':'apple','b':'banana'}
print(fruits)
fruits['a']='apricot'
print(fruits)

#class dictionary
dict_nums=dict({1:10,2:20,3:30})
print(dict_nums)
print(dict_nums[3])

#Methods
#update()
fruits={'a':'apple','b':'banana'}
fruits.update({'c':'cherry'})
print(fruits)

#pop()
fruits={'a':'apple','b':'banana','c':'cherry'}
fruits.pop('b')
print(fruits)

#popitem()
fruits={'a':'apple','b':'banana','c':'cherry'}
fruits.popitem()
print(fruits)

#clear()
fruits={'a':'apple','b':'banana','c':'cherry'}
fruits.clear()
print(fruits)

#Access related methods
#get()
fruits={'a':'apple','b':'banana','c':'cherry'}
print(fruits.get('b'))

#keys()
fruits={'a':'apple','b':'banana','c':'cherry'}
print(fruits.keys())

dict_nums={1:10,2:20,3:30}
only_keys=dict_nums.keys()
for i in only_keys:
    print(i)

#values()
fruits={'a':'apple','b':'banana','c':'cherry'}
print(fruits.values())

dict_nums={1:10,2:20,3:30}
only_values=dict_nums.values()
for i in only_values:
    print(i)

#items()
fruits={'a':'apple','b':'banana','c':'cherry'}
print(fruits.items())

#copy()
dict_nums={1:10,2:20,3:30}
bk_dict_nums=dict_nums.copy()
print(dict_nums)
print(bk_dict_nums)
bk_dict_nums.update({4:40})
print(bk_dict_nums)

#soft copy using assignment 
dict_nums={1:10,2:20,3:30}
bk_dict_nums=dict_nums
bk_dict_nums.update({4:40})
print(dict_nums)
print(bk_dict_nums)

#set default()
dict_nums={1:10,2:20,3:30}
print(dict_nums)
dict_nums.setdefault(4,400)
print(dict_nums)
dict_nums.setdefault(3,300)
print(dict_nums)