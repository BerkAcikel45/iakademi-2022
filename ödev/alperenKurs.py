from abc import abstractmethod, ABC
import random

student_ids = []
students = {}
teachers = {}
courses = {}


class Student(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # Only for students
    @abstractmethod
    def set_id(self):
        pass

    @abstractmethod
    def print_all(self):
        pass

    @abstractmethod
    def add_student(self):
        pass


class Courses(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def delete_course(self):
        pass


class Teacher:
    def __init__(self, name, last_name, password, email, address, number, course):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.address = address
        self.number = number
        self.course = course

    def print_all(self):
        for i in teachers:
            print(f"{teachers[i]['name']} {teachers[i]['last_name']} {teachers[i]['email']} {teachers[i]['address']} {teachers[i]['number']} {teachers[i]['course']}")

    def add_teacher(self):
        teachers[self.name] = {
            "name": self.name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
            "address": self.address,
            "number": self.number,
            "course": self.course
        }


class Student(Teacher):
    def __init__(self, name, last_name, password, email, address, number, course):
        super().__init__(name, last_name, password, email, address, number, course)

    def set_id(self):
        self.id = random.randint(1, 1000)
        while self.id in student_ids:
            self.id = random.randint(1, 1000)
        student_ids.append(self.id)
        return self.id

    # Overriden method
    def print_all(self):
        for i in students:
            print(
                f"{students[i]['Student ID']} - {students[i]['Student Name']} {students[i]['Student Lastname']} - {students[i]['Student PW']} - {students[i]['Student mail']} - {students[i]['Student Address']} - {students[i]['Courses']}")

    def add_student(self):
        id_generator = self.set_id()
        students[id_generator] = {
            'Student ID': id_generator,
            'Student Name': self.name,
            'Student Lastname': self.last_name,
            'Student PW': self.password,
            'Student mail': self.email,
            'Student Address': self.address,
            'Student Number': self.number,
            'Courses': [self.course]
        }


class Course:
    def __init__(self, name, teacher, students, length, offering):
        self.name = name
        self.teacher = teacher
        self.students = students
        self.length = length
        self.offering = offering

    def add_course(self):
        courses[self.name] = {
            'Course Name': self.name,
            'Teacher': [self.teacher],
            'Students': [self.students],
            'Length': self.length,
            'Offering': self.offering
        }

    def delete_course(self):
        for i in courses:
            print(
                f"{courses[i]['Course Name']} - {courses[i]['Teacher']} - {courses[i]['Students']} - {courses[i]['Length']} hour(s) - {courses[i]['Offering']}")

        delete_input = input("Enter name of the course you want to delete: ")

        if delete_input in courses:
            courses.pop(delete_input)
            print("Course deleted successfully!")
        else:
            print("Such course does not exist!")


while True:
    get_operation = input("Please choose your action: ")

    # Create and save a new student
    if get_operation == "1":
        stu = Student(
            f"{input('Enter student name:')}", f"{input('Enter student last name: ')}",
            f"{input('Create a password: ')}", f"{input('Enter student mail: ')}",
            f"{input('Enter student address: ')}", f"{input('Enter student contact: ')}",
            ""
        )
        stu.add_student()

    # Print all students
    elif get_operation == "2":
        try:
            stu.print_all()

        # Just in case user tries to view students before creating at least one student
        except NameError:
            print("No students to show...")

    # Create a course
    elif get_operation == "3":
        print("CREATE A COURSE")
        crs = Course(
            f"{input('Enter course name: ')}",
            f"{input('Enter teacher(s): ')}", f"{input('Enter course students: ')}", f"{input('Enter course length: ')}", f"{input('Enter course offerings: ')}"
        )

        crs.add_course()

    # Delete a course
    elif get_operation == "4":
        try:
            crs.delete_course()

        # Just in case user tries to view courses before creating at least one course
        except NameError:
            print("No courses to delete...")

    # Create and add the created teacher to an existing course
    elif get_operation == "5":
        print("CREATE A TEACHER")
        tcr = Teacher(
            f"{input('Enter teacher name: ')}", f"{input('Enter teacher last name: ')}", f"{input('Create a password: ')}", f"{input('Enter teacher mail: ')}", f"{input('Enter teacher address: ')}", f"{input('Enter teacher contact: ')}", f"{input(f'Enter teacher course: ')}"
        )
        tcr.add_teacher()

        if tcr.course in courses:
            print(f"Teacher added to {tcr.course} successfully!")
            courses[tcr.course]['Teacher'].append(tcr.name)
        else:
            print("Such course does not exist!")

    # Remove a teacher from a course
    elif get_operation == "6":
        print("YOU ARE ABOUT TO REMOVE A TEACHER FROM A COURSE")
        get_course = input("Select a course first: ")
        get_teacher = input("Now select the teacher: ")

        for i in courses:
            if get_course == courses[i]['Course Name']:
                try:
                    courses[i]['Teacher'].remove(get_teacher)
                    print("Removed successfully!")
                except NameError:
                    print("ERROR!")

    # Remove a student from a course
    elif get_operation == "7":
        print("YOU ARE ABOUT REMOVE A STUDENT FROM A COURSE")

        get_course = input("Select a course first: ")
        if get_course in courses:
            get_student = input("Now select a student: ")

            removed_stu = courses[get_course]['Students'].remove(get_student)
            print(f"Successfully removed {get_student} from system")
        else:
            print(
                "Such student/course doesn't exist or is not registered to any of our courses.")

    # Add a student to an existing course
    elif get_operation == "8":
        print("YOU ARE ABOUT TO ADD A STUDENT TO A COURSE")

        stu.print_all()
        get_course = input("Select a course first: ")
        get_student = int(input("Now select the student by ID: "))

        for i in courses:
            if get_course == courses[i]['Course Name'] and get_student in student_ids:
                courses[get_course]['Students'].append(
                    students[get_student]['Student Name'])

                students[get_student]['Courses'].append(get_course)

                print(f"{get_student} added to {get_course} successfully!")
            else:
                print("Such course or student does not exist!")

    elif get_operation == "10":
        print("You have chosen to exit the program...")
        break
    else:
        print("Invalid command!")
