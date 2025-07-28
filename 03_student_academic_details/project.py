#a simple system that stores and processes a student’s academic and attendance detail
#Declare variables
student_ID=123
student_name='Ram'
student_age=20
quiz_score=80
assignment_score=75
exam_score=60
student_attendence=65

#Using arithmetic operators
total_score=quiz_score+assignment_score+exam_score
average_score=total_score/3

#Using relational operators
student_passed=average_score>75
print('Student passed with:', student_passed)

#Using increment operator 
student_attendence+=1
print('Student Attendence;', student_attendence)

#Using logical operators
award_eligibility=student_attendence>60 and student_passed

#Display results
print('Student_name:', student_name)
print('Student_age:', student_age)
print('Student_ID:', student_ID)
print('Quiz_score:', quiz_score)
print('Assignment_score:', assignment_score)
print('Exam_score:', exam_score)
print('Total_score:', total_score)
print('Average_score:', average_score)
print('Passing Status:', student_passed)
print('Award_eligibility:', award_eligibility)