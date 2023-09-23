class studen:
  
 def__init__(self,name,roll_number,cgpa):
    self.name=name 
    self.roll_number=roll_number
    self.cgpa=cgpa


def sort_srudents(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
key =lambda student: student.cgpa, 
                           reverse=True)
return sorted_students
#example usage:
students =[
     student("vishva", "B240", 8.8), ￼
￼    student("manisha"," B241", 8.9), 
     student("mathu", "B242", 9.2), 
     student("siva"," B243", 9.3), 
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".Format student.name, student.roll_number, student. cgpa)) 
