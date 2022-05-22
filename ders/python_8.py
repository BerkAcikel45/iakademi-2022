# class Footballer:
#     # Attributes
#     name = "Messi"
#     team = "Paris"
#
# f1 = Footballer()
# print(f1.name)
# print(f1.team)
#
# f1.team = "A team"
# print(f1.name)
# print(f1.team)
# print(f1)
# print(type(f1))
#

class Square(object):
    # edge = 5

    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge * self.edge


s1 = Square(7)
s2 = Square(5)
s3 = Square(10)

print(s1.area())
print(s2.area())
print(s3.area())


class Animal:
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


dog = Animal(a="Dog", b=3)
cat = Animal("Cat", 1)

print(dog.getName())
print(cat.getName())


class Calculater:

    def __init__(self, number_1: int, number_2: int) -> None:
        self.num_1 = number_1
        self.num_2 = number_2

    def sum(self):
        return self.num_1 + self.num_2

    def subs(self):
        return self.num_1 - self.num_2

    def div(self):
        return self.num_1 / self.num_2

    def multiply(self):
        return self.num_1 * self.num_2


# while True:
#     number_1 = int(input("Enter integer 1: "))
#     number_2 = int(input("Enter integer 2: "))
#     operation = input("Enter operation")
#
#     c1 = Calculater(number_1, number_2)
#
#     if operation == "+":
#         print(c1.sum())
#     elif operation == "-":
#         print(c1.subs())
#     elif operation == "/":
#         print(c1.div())
#     elif operation == "*":
#         print(c1.multiply())

# c1 = Calculater(5,2)
# c2 = Calculater(10, 5)
#
# print(c1.div())
# print(c1.sum())
# print(c2.div())
# print(c2.sum())


# encapsilation

class BankAccount:

    def __init__(self, name, address, money):
        self.name = name
        self.address = address
        self.__money = money

    def GetMoney(self):
        return self.__money

    def SetMoney(self, amount):
        self.__money = amount


p1 = BankAccount("messi", "barcelona", 1000)
p2 = BankAccount("ronaldo", "paris", 2000)

print(f"Name: {p1.name} Money: {p1.GetMoney()}")
print(f"Name: {p2.name} Money: {p2.GetMoney()}")

p2.SetMoney(p1.GetMoney() + p2.GetMoney())
# print(p1.money)
p1.SetMoney(0)

print(f"Name: {p1.name} Money: {p1.GetMoney()}")
print(f"Name: {p2.name} Money: {p2.GetMoney()}")


# inheritance

class Animal:
    def __init__(self):
        print("Animal Created")

    def toString(self):
        print("Animal")

    def walk(self):
        print("Animal Walk")


class Monkey(Animal):

    def __init__(self):
        super(Monkey, self).__init__()
        print("Monkey Created")

    def toString(self):
        print("Monkey")

    def climb(self):
        print("Climbing")


class Bird(Animal):

    def __init__(self):
        super(Bird, self).__init__()
        print("Bird Created")

    def toString(self):
        print("Bird")

    def fly(self):
        print("Flying..")


m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()

b1 = Bird()
b1.toString()
b1.walk()
b1.fly()


class Website:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def login(self):
        print(f"Welcome {self.name} {self.surname}")


class Website2(Website):
    def __init__(self, name, surname, id):
        super(Website2, self).__init__(name, surname)
        self.id = id

    def login(self):
        print(f"Welcome {self.name} {self.surname} {self.id}")


class Website3(Website):
    def __init__(self, name, surname, email):
        super(Website3, self).__init__(name, surname)
        self.email = email

    def login(self):
        print(f"Welcome {self.name} {self.surname} {self.email}")


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Bird(Animal):

    def __init__(self):
        print("Bird Crteated")

    def run(self):
        print("Running")

    def walk(self):
        print("Walking")

    def fly(self):
        print("Flying")


b1 = Bird()
b1.walk()
b1.run()
b1.fly()


class Employee:

    def Raise(self):
        raise_rate = 0.1
        return 100 + 100 * raise_rate


class ComputerEngineer(Employee):

    def Raise(self):
        raise_rate = 0.2
        return 100 + 100 * raise_rate


class Manager(Employee):

    def Raise(self):
        raise_rate = 0.3
        return 100 + 100 * raise_rate


class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge * self.edge

    def perimeter(self):
        return self.edge * 4

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius


square = Square(5)
print(square.area())
print(square.perimeter())

circle = Circle(2)
print(circle.area())
print(circle.perimeter())



"""
1) Create Student
2) Display Students
3) Add Course
4) Drop Course
5) Modify Course
6) Remove Student From Course
7) View Registered Courses
8) View Course Offering Roster
9) Add course Teacher
10) Exit 

Student:
Name,
Lastname,
Password,
email,
address,
contactNumber,
studentId,
RegisteredCourses

Teacher:
Name,
Lastname,
Password,
email,
address,
contactNumber,
RegisteredCourses

Course:
name,
teacher,
students,
course_hour


"""
