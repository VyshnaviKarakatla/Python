student_ID=int(input("Enter Student ID:"))
student_name=input("Enter Student Name:")
student_attendance=int(input("Enter Student Attendance:"))
number_of_subjects=int(input(("Enter Number OF Subjects")))

score = int(input("Enter score for subject 1: "))
total_score = score

subjects=2
while subjects<=number_of_subjects:
    score=int(input(f"Enter score for subject {subjects}:"))
    user=input("Type yes to continue ")
    total_score += score
    if (str(user)) == "yes":
        print("Thank you")
    subjects+=1
    if subjects>number_of_subjects:
        break
print("Total Score:", total_score)

#Average score
avg_score=total_score/number_of_subjects
print(avg_score)

#Performance Level
if avg_score>=85:
    print("Excellent")
    Performance_level="Excellent"
elif avg_score>=70 and avg_score<=84:
    print("Good")
    Performance_level="Good"
elif avg_score>=50 and avg_score<=69:
    print("Average")
    Performance_level="Average"
else:
    print("Needs Improvement")
    Performance_levl="Needs Improvement"


#Attendance status
if student_attendance<=75:
    print("WARNING:Needs to improve attendance")
    Attendance="WARNING:Needs to improve attendance"
else:
    print("OK")
    Attendance="OK"

#Display Final Results
print("Student Final Results:")
print(f"Student ID: {student_ID}")
print(f"Student Name: {student_name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {avg_score}")
print(f"Performance Level: {Performance_level}")
print(f"Attendance: {Attendance}")