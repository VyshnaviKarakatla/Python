#Control Statements
#if
#Checking if number given is positive
num=10
if num>0:
    print(f'The given number is {num} and it is positive.')

#Check if the number is in range(10-20)
N=int(input("Enter a number:"))
if N>10 and N<20:
    print("Yes, the entered number is in the range")


#if-else
#Checking if given value is positive or negative
number=25
if number>0:
    print(f'The given number {number} is positive')
else:
    print(f'The given number {number} is negative')

#Check vote eligibility
Age=int(input("Enter age:"))
if Age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#elif statement
#Grade based on the average score
avg_score=int(input("Enter your average score:"))
if avg_score>=90 and avg_score<=100:
    print("A GRADE")
elif avg_score>=75 and avg_score<=89:
    print("B GRADE")
elif avg_score>=60 and avg_score<=74:
    print("C GRADE")
elif avg_score>=35 and avg_score<=59:
    print("D GRADE")
else:
    print("FAIL")


#Match case
choice=int(input("Enter a number of your choiice:"))
match choice:
    case 1:
     print("One")
    case 2:
     print("Two")
    case 3:
     print("Three")
    case 4:
     print("Four")
    case _:
     print("Invalid")

#Nested if
#Club entry-if age is 21 or above and also a valid ID should be present
age=int(input("Enter your age:"))
has_ID=True
if age>=21:
    print("You are eligible")
    if has_ID:
        print("You are allowed")
    else:
        print("You are not allowed")
else:
    print("You are not eligible")
