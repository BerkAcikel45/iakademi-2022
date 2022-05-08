message = "c"


def greet(name):
    global message
    message = "a"


a = greet("Berk")
print(message)

print(a)

def artikyil(yil):
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
        else:
            return True


for year in range(1900, 2020):
    if artikyil(year):
        print(f"{year} bir artık yıldır.")

list_1 = [3, 5, 27, 55]

list_2 = ["berk", 12312, 0.0]

list_1 = []
list_1 = list()

print(len(list_1))

print(list_2[0])
print(list_2[-1])


list_4 = [12, 25, 555, 231, "Apple", "Orange"]

print(list_4[0:4])
print(list_4[:4])
print(list_4[3:])
print(list_4[::2])
print(list_4[::-1])

# [start:stop:step]
print(list_4[1::2])


numberList = [25, 11, 232, 555]
numberList_2 = [124, 4444, 2221, 555533, 21]

print(numberList + numberList_2)
print(numberList_2 + ["Apple"])


list_5 = numberList + numberList_2

print(list_5)


list_5[0] = 24

print(list_5)


list_5[:2] = [10, 5]

print(list_5)


print(list_5 * 3)


list_5.append("Berk")
list_5.append("Ali")

print(list_5)

list_5.pop()

print(list_5)

list_5.pop(0)

print(list_5)

list_5.remove("Berk")
print(list_5)

print(list_5.count(21))

print(list_5)

list_5.insert(3, 44)
print(list_5)


list_5.extend([231231,"ABC","BBC", "121412"])

print(list_5)

list_5.sort()
#list_5.reverse()

print(list_5)

list_5.clear()
print(list_5)

index = 0
names = []

while True:
    if index == 5:
        break

    input_1 = input("Enter Name: ")
    if input_1 in names:
        print(input_1, "already exist.")
    else:
        names.append(input_1)
        index += 1

print(names)
















