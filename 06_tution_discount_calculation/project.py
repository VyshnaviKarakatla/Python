#Tuition Discount Calculation in Python
Student_name=input("Enter student name:")
Student_grade_level=int(input("Enter student grade level:"))
Student_base_tution_fee=int(input("Enter base tution fee of student:"))
Student_discount=float(input("Enter discount percentage:"))
Student_academic_score=int(input("Student academic score:"))

#Discount Calculation
if Student_academic_score>=90 and Student_academic_score<=100:
    Student_academic_status=True
    print("Student Topper:", Student_academic_status)
if Student_grade_level>=1 and Student_grade_level<=12:
    if Student_grade_level>=9 and Student_grade_level<=12:
        if Student_academic_score>=90 and Student_academic_score<=100:
            discount_for_topper_in_grade_9_to_12=(Student_base_tution_fee)*2/100
            print("Student is Topper, so discount:",discount_for_topper_in_grade_9_to_12)
            Total_discount_for_topper_in_grade_9_to_12=Student_discount+discount_for_topper_in_grade_9_to_12
            print("Total_discount:",Total_discount_for_topper_in_grade_9_to_12)
            print(f"Student discount: {Total_discount_for_topper_in_grade_9_to_12}")
            Tution_fee=Student_base_tution_fee-Total_discount_for_topper_in_grade_9_to_12
            print(f"Total tutionn fee: {Tution_fee}")
        else:
            discount_for_not_topper_but_in_grade_9_to_12=(Student_base_tution_fee)*1/100
            print("Student is not a topper,so discount:",discount_for_not_topper_but_in_grade_9_to_12)
            Total_discount_for_not_topper_in_grade_9_to_12=Student_discount+discount_for_not_topper_but_in_grade_9_to_12
            print("Total_discount:",Total_discount_for_not_topper_in_grade_9_to_12)
            print(f"Student discount: {Total_discount_for_not_topper_in_grade_9_to_12}")
            Tution_fee=Student_base_tution_fee-Total_discount_for_not_topper_in_grade_9_to_12
            print(f"Total Tution fee: {Tution_fee}")
    if Student_grade_level>=6 and Student_grade_level<=8:
        Student_discount_for_6_to_8=(Student_base_tution_fee)*5/100
        Total_discount_for_6_to_8=Student_discount+Student_discount_for_6_to_8
        print("Total disocunt:",Total_discount_for_6_to_8)
    else:
        if Student_grade_level<6 and Student_grade_level>=1:
         print("Student is not eligible for any disocunt")
else:
    print("Student grade level is not between 1,12")

#Additional Discount
print("Options:")
print("Select 1 if student is in grade 10")
print("Select 2 if student is in grade 12")
print("Select 3 or 4 for any other grades")
Grade=int(input("Enter option 1-4"))
match Grade:
    case 1:
        if Student_grade_level==10:
            print("Additional dicount:3%")
    case 2:
        if Student_grade_level==12:
            print("Additioanl disocunt:5%")
    case 3:
        if Student_grade_level!=10:
            print("No additional discount")
    case 4:
        if Student_grade_level!=12:
            print("No additional discount")
    case _:
        print("Invalid Optiion")


print("Student Summary")
print(f"Student Name: {Student_name}")
print(f"Student Grade Level: {Student_grade_level}")
print(f"Academic Topper: {Student_academic_score}")
print(f"Base Tution fee:{Student_base_tution_fee}")
print(f"Student Discount: {Student_discount}")