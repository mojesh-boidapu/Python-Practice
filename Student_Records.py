#To add a new student details using functions
student_data=[{"Name":"Mojesh",
               "roll_no":22,
               "Age":21,
               "course":"Python"},
              {"Name":"Manoj",
               "roll_no":15,
               "Age":22,
               "course":"Python"
              }]
def new_student_data(name,roll_no,age,course):
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=roll_no
    new_student["Age"]=age
    new_student["course"]=course
    student_data.append(new_student)
    print(student_data,end='\n')
end=False
while not end:
    name=input("Enter a student name:")
    roll_no=input("Enter a roll no:")
    age=input("Enter a age:")
    course=input("Enter a course:")
    new_student_data(name=name,roll_no=roll_no,age=age,course=course)
    want_to_add=input("Do you want to add another student?(yes/no):")
    if want_to_add=='yes' or want_to_add=='y':
        end=False
    elif want_to_add=='no' or want_to_add=='n':
        end=True
    else:
        end=True