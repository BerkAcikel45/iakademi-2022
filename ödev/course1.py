class Student:
    def __init__(self, name, lastname, password, email, address, contactNumber, registeredCourse):
        self.name = name
        self.lastname = lastname
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
        self.registeredCourse = registeredCourse

    def create_student(self, dict_student):
        dict_student = dict(name=self.name, last_name=self.lastname, password=self.password, email=self.email, address=self.address, \
                            contact_number=self.contactNumber, registered_course=self.registeredCourse)
            return dict_student



# while True:
list_student = []


s1 = Student(name=input("enter your name"), lastname=input("enter last name"), password=input("enter a password"),\
             email=input("enter your email"), address=input("enter your address"), contactNumber=input("enter your contact number"),\
             registeredCourse=input("enter course name"))
    # if s1.name == "q":
    #     break

list_student.append(Student.create_student(s1))

print(list_student)