
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students = 0
    students_list = []

    def __init__(self, student_number, student_name, student_age):
        self.student_id = random.randint(1000, 9999)
        self.student_number = student_number
        self.student_name = student_name
        self.student_age = student_age
        self.courses_list = []

        Student.total_students += 1
        Student.students_list.append(self)

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if self.courses_list else 0


def exit_program():
    print("Exiting the program.")
    exit()


students = []

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
        students.append(student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                students.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                print("Student Details:", student.get_student_details())
                break
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                print("Student Average Mark:", student.get_student_average())
                break
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students:
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
