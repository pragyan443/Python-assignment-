students = []

def add_student(student_details):
    students.append(student_details)

def create_student(i, student_id, name, grade):
    student_details = {
        f"Id_st{i+1}": student_id,
        f"Name_st{i+1}": name,
        f"Grade_st{i+1}": grade
    }
    return student_details

def is_duplicate_id(student_id):
    return any(student_id in student.values() for student in student)
n = int(input("Enter the number of students: "))
print("Enter student details:")

for i in range(n):
    student_id = input("Enter student ID: ")
    
    if is_duplicate_id(student_id):
        print("Duplicate ID found. Please enter a unique ID.")
        continue

    name = input("Enter student Name: ")
    grade = input("Enter student Grade: ")
    
    student_details = create_student(i, student_id, name, grade)
    add_student(student_details)
    print("Student added successfully.\n")

print("\nList of Students:")
for i, student in enumerate(students, 1):
    print(f"Student {i}: {student}")
