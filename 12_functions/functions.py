#Positinal arguments
def login(username,password):
    if username=='vyshu' and password=='2000':
        print("Login Success")
    else:
        print("Login Failed")
login('vyshu','2000')

#Default arguments
def emp_info(emp_name,emp_email,emp_loc='Hyderabad'):
    print(f"Hi {emp_name}, your email is {emp_email} and your loction is {emp_loc}")
emp_info('vyshu','vyshu@gmail.com')
#Overridden
def emp_info(emp_name,emp_email,emp_loc='Hyderabad'):
    print(f"Hi {emp_name}, your email is {emp_email} and your loction is {emp_loc}")
emp_info('vyshu','vyshu@gmail.com','Pune')

#Keyword arguments
def emp_info(emp_name,emp_email,emp_loc):
    print(f"Hi {emp_name}, your email is {emp_email} and your loction is {emp_loc}")
emp_info(emp_name='vyshu',emp_loc='Hyderabad',emp_email='vyshu@gmail.com')

#Arbitary positional arguments(*args)
def add_all(*numbers):
    total=0
    for i in numbers:
        total+=i
    print(f"Total is: {total}")
add_all(1)
add_all(1,2)
add_all(1,2,30,47,20)

#Arbitary keyword arguments(**kwargs)
def profile(**info):
    print(info)
profile(id=101)
profile(id=101,name='vyshu')
profile(id=101,name='vyshu',loc='Hyd')

#Using both (*args) and (**kwargs)
def trans(*month,**numberof):
    print(month)
    print(numberof)
    total=0
    for i in month:
        total+=i
    print(f"Hi {numberof['name']}, your employee ID is {numberof['id']}. You transactions for {len(month)}months have {total}")
trans(1000,2000,3000,name='vyshu',id=101)