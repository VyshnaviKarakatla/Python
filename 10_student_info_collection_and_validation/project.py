#Student Information Collection & String Validation
#Student ID Validation
print("-"*20)
print("Enhanced LMS Grade Tracker")
print("-"*20)
student_id_valid=False
while not student_id_valid:
    student_id=input("Enter student ID(numbers only): ")
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please input positive values only")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id>0:
            student_id_valid=True
        else:
            print("Please input a non-zero value")
    else:

        print("Enter only numbers")

#professioanl ID
professional_id="STU"+ str(student_id).zfill(5)
print(professional_id)

#Student Name Validation
student_name_valid=False
while not student_name_valid:
    student_name=input("Enter student name: ")
    student_name=student_name.strip().title()
    #to remove space in between name
    name_check=student_name.replace(" ","")
    #only alphabets
    if name_check.isalpha() and len(student_name)>=3:
        student_name_valid=True
        print("Name:" + student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain only letters")
        elif len(student_name) <3:
            print("Name should have atleast 3 letters")

#Email generation
name_part=student_name.split()
first_name=name_part[0].lower()
student_email=first_name+"."+str(student_id)+"@university.edu"
print(student_email)

#Discount calculation
base_course_fee_valid=False
while not base_course_fee_valid:
    base_course_fee=input("Enter Course fee: ")
    if base_course_fee.startswith("-") and base_course_fee[1:].isdigit():
        print("Please input positive values only")
    elif base_course_fee.isdigit():
        base_course_fee=int(base_course_fee)
        if base_course_fee>0:
            base_course_fee_valid=True
        else:
            print("Please input a non-zero value")
    else:

        print("Enter only numbers")

discount=0
print("Enter description: ")
description=input()
if description.lower().find("reference")!=-1:
    discount+=5000
if "scholarship" in description:
    discount+=7000
if "promo" in description:
    discount+=3000
final_fee=base_course_fee-discount

print("Base Course Fee: "+str(base_course_fee))
print("Discount: "+str(discount))
print("After Discount Pay:"+str(final_fee))