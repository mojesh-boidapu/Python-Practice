#create a marks sheet
student_marks={
     'Naruto':67,
     'Luffy':52,
     'Ichigo':95,
     'Tanjiro':84,
     'Deku':75,
     'Eren':47,
     'Goku':39,
 }
student_grades={}
for student in student_marks:  #Here it only axis 'keys' means names not the values(marks),SO
     marks=student_marks[student]
     if marks>90:
         student_grades[student]='A+'
     if marks>80:
         student_grades[student]='A'
     if marks>70:
         student_grades[student]='B+'
     if marks>60:
         student_grades[student]='B'
     if marks>50:
         student_grades[student]='C'
     if marks>40:
         student_grades[student]='D'
     else:
         student_grades[student]='F'
print(student_grades)