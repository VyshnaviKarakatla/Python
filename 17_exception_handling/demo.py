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

#userdefined error-single error
class AgeTooYoungerError(Exception):
    pass
age=int(input("Enter age: "))
if age<18:
    raise AgeTooYoungerError("You must have 18+ to register")
else:
    print("Registration Successful")

#userdefined error-multiple error
class AgeTooYoungerError(Exception):
    pass
class NoIDError:
    pass
age=int(input("Enter age: "))
if age<18:
    raise AgeTooYoungerError("You must have 18+ to register")
else:
    has_id=input("Do you have ID? (yes/no)")
    if has_id!='yes':
        raise NoIDError("You must have ID")
    
#userdefined error-handling with try,except,else,finally
class AgeTooYoungerError(Exception):
    pass
class NoIDError(Exception):
    pass
age=int(input("Enter age: "))
try:
    if age<18:
        raise AgeTooYoungerError
    else:
        has_id=input("Do you have ID? (yes/no): ")
        if has_id=='no':
            raise NoIDError
        else:
            pass
except AgeTooYoungerError:
    print("You must have 18+ to register")
except NoIDError:
    print("You must have ID")
else:
    print("Registration Success")
finally:
    print("Thank you!!!")