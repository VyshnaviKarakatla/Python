#Sets
#empty set
empty_set={}
print(type(empty_set))

empty_set=set()
print(type(empty_set))

#number set
nums_set={10,20,30,40,50}
print(nums_set)
print(type(nums_set))

#duplicates eliminated
nums_set={10,20,30,40,50,10,20,30}
print(nums_set)

#text data
text_set={'python','java','js'}
print(text_set)

#mixed data
mixed_set={10,'python',20,'java',30}
print(mixed_set)

#Accessing data
set_nums={10,20,30,40,50}
for i in set_nums:
    print(i)
list_nums=list(set_nums)
print(list_nums)
print((list_nums[1]))

#add()
s1={10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
s1.add(70)
print(s1)

#update()
s1={10,20,30,40,50}
s1.update([60,70,80,90,100])
print(s1)

#remove()
s1={10,20,30,40,50}
s1.remove(50)
print(s1)

#discard()
s1={10,20,30,40,50}
s1.discard(50)
print(s1)
s1.discard(70)
print(s1)

#clear()
s1={10,20,30,40,50}
s1.clear()
print(s1)

#pop()
s1={10,20,30,40,50}
s1.pop()
print(s1)

#Set specific operations
s1={10,20,30,40,50}
s2={40,50,60,70,80}
#union()
print("UNION")
print(s1.union(s2))
print(s1|s2)

#intersection()
print("INTERSECTION")
print(s1.intersection(s2))
print(s1&s2)

#intersection_update()
print("INTERSECTION UPDATE")
print(s1)
print(s2)
print(s1.intersection_update(s2))
print(s2.intersection_update(s1))
print(s1)
print(s2)

#difference()
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print("DIFFERENCE")
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)

#difference_update()
print("DIFFERENCE UPDATE")
print(s1)
print(s2)
print(s1.difference_update(s2))
print(s2.difference_update(s1))
print(s1)
print(s2)

#symmetric_difference
print("SYMMERIC DIFFERENCE")
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s2.symmetric_difference(s1))
print(s2^s1)

#symmetric_difference_update()
print("SYMMETRIC DIFFERENCE UPDATE")
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print(s2.symmetric_difference_update(s1))
print(s1)
print(s2)

#issubset()
s1={10,20,30,40,50}
s2={40,50}
print(s2.issubset(s1))

#issuperset()
print(s1.issuperset(s2))
print(s2.issuperset(s1))

#isdisjoint()
s1={10,20,30}
s2={20,30}
s3={40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

#copy()
s1={10,20,30,40,50}
s2=s1
print(s1)
print(s2)
s2.add(60)
print(s2)
print(s1)

#frozen set
fs=frozenset({10,20,30,40,50})
print(fs)
print(type(fs))