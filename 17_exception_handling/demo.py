print("Program Started")
a=10
b=5
c=a/b
print(c)
print("Program Completed")
print('-'*25)

# print("Program Started")
# a=10
# #b=0 #ZeroDivisionError
# c=a/b
# print(c)
# print("Program Completed")

#try and except for single error
print("Program Started")
a=10
b=0
try:
    print(a/b)
except:
    print("OOPS!")
print("Program Completed")
print('-'*25)

#try and except for multiple error
import sys
print("Program Started")
data=[2,4,'python',0,8]
for i in data:
    try:
        print(1/i)
    except:
        print("OOPS!")
        print(sys.exc_info())
print("Program Completed")
print('-'*25)

#try and except for known multiple error
print("Program Started")
data=[2,4,'python',0,8]
for i in data:
    try:
        print(1/i)
    except TypeError:
        print("OOPS! There is a TypeError")
    except ZeroDivisionError:
        print("OOPS! There is a ZeroDivisionError")
print("Program Completed")
print('-'*25)

#else without error
print("Program Started")
a=10
b=5
try:
    print(a/b)
except:
    print("OOPS!")
else:
    print("Calculation Success")
print("Program Completed")
print('-'*25)

#else with error
print("Program Started")
a=10
b=0
try:
    print(a/b)
except:
    print("OOPS!")
else:
    print("Calculation Success")
print("Program Completed")
print('-'*25)

#finally without error
print("Program Started")
a=10
b=5
try:
    print(a/b)
except:
    print("OOPS!")
else:
    print("Calculation Success")
finally:
    print("Program Completed")
print('-'*25)

#finally with error
print("Program Started")
a=10
b=0
try:
    print(a/b)
except:
    print("OOPS!")
else:
    print("Calculation Success")
finally:
    print("Program Completed")
print('-'*25)