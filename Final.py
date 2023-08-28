Name = "yousef Iyad ALhassani"
Delivery_Date = "30/8/2023"
"Eng.Mohanad Alkrunz"

course_id_counter = 1
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark
class Student:
    total_students = 0
    students_list = []

    def __init__(self):
        self.student_id = random.randint(1000, 9999)
        self.student_name = input("Enter student name: ")
        self.student_age = int(input("Enter student age: "))
        self.student_number = input("Enter student number: ")
        self.courses_list = []

        Student.total_students += 1
        Student.students_list.append(self)

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        return [(course.course_name, course.course_mark) for course in self.courses_list]

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if self.courses_list else 0

students = []

while True:
    choice = input("Do you want to add a new student? (yes/no): ")

    if choice.lower() == "no":
        break

    student = Student()
    students.append(student)

    while True:
        course_name = input("Enter course name (or 'done' to finish adding courses): ")
        if course_name.lower() == "done":
            break
        course_mark = float(input("Enter course mark: "))
        course = Course(course_name, course_mark)
        student.enroll_course(course)

for student in students:
    print("\nStudent Details:", student.get_student_details())
    print("Student Courses with Marks:")
    for course_name, course_mark in student.get_student_courses():
        print(f"Course: {course_name}, Mark: {course_mark}")
    print(f"Student Average Mark: {student.get_student_average():.2f}\n")
while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Age. Please enter a valid number.")

        student = Student(student_number, student_name, student_age)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in Student.students_list:
            if student.student_number == student_number:
                Student.students_list.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in Student.students_list:
            if student.student_number == student_number:
                print("Student Details:", student.get_student_details())
                break
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in Student.students_list:
            if student.student_number == student_number:
                print("Student Average Mark:", student.get_student_average())
                break
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in Student.students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                course = Course(course_name, course_mark)
                student.enroll_course(course)
                print("Course Added to Student Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 6:
        exit_program()

    else:
        print("Invalid selection. Please choose a valid option.")