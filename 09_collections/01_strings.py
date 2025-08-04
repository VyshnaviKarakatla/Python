#Strings-Sequence of characters
data_1='hello'
data_2="hello"
data_3='''hello'''
data_4="""hello"""
print(data_1)
print(data_2)
print(data_3)
print(data_4)

#Use of multi-line Strings
#single-line
#des="Python is a high-level, general-purpose programming language. 
#Its design philosophy emphasizes code readability with the use of 
#significant indentation."
#Noot taking last 2 lines

#multi-line
des="""Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of 
significant indentation."""
#takes whole string

#Use cases of '',"",''' ''',""" """
question="How are you?"
#answer='i'm fine' #TypeError
answer="i'm fine"
print("answer")
#ans="iam fine and "good"" #TypeError
ans='iam fine and "good"'
print(ans)
answer_1='''I'm fine and "good"'''
answer_2="""I'm fine and 'good'"""
print(answer_1)
print(answer_2)


#String Indexing and String Slicing
#String Indexing
text="python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[5])
#print(text[6]) #IndexError
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])

#String Slicing
text="python"
print(text[0:3])
print(text[1:5])
print(text[1:])
print(text[:4])
print(text[:])
print(text[1:4])
print(text[1:4:1])
print(text[1:5:2])
print(text[-4:-1])
print(text[-4:-1:1])
print(text[-4:1:-1])
print(text[::-1])
print(text[-2:-5:1])
print(text[4:0:-1])
print(text[-2:-6:-1])

#String Mutablity
#a="Name"
#a[1]="A" #TypeError as Strings can't be changed

#String Reassigning
a="Age"
a="School"
print(a)

#Cancat(+) and Repeat(*)
str="hi"
print(str *5)

#String Methods
#To know the string methods we use
print(dir(str))

mobile_number=input("Enter Mobile Number: ")
valid_number=mobile_number.isdigit()
print(valid_number)

PAN=input("Enter PAN Number: ")
valid_PAN=PAN.isalnum()
print(valid_PAN)

PAN_Number=input("Enter PAN Number: ")
PAN_Number.upper()
print("PAN_Number", PAN_Number.upper())

#To know about any method functionality
print(help(str.upper()))