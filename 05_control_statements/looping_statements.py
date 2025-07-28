#Loops
#while
count=1
while count<=5:
    print(count)
    count+=1

#for
for i in range(11):
    print(i)


#printing even numbers from 1 to 20 using while loop and for loop
#while
num=2
while num<=22:
    print(num)
    num+=2

#for
for i in range(2,22,2):
    print(i)


#Nested while loop
#printing math table
i=1
while i<=4:
    j=1
    while j<=10:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i+=1

#Netsed for loop
#printing math table
for i in range(5):
    for j in range(11):
        print(f"{i} x {j} = {i*j}")