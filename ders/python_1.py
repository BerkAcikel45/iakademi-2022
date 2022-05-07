
print("Hello World")

number = 10

print(type(number))

number = 10.5

print(type(number))

print(10 / 5)
print(type(10 / 5))

print(10 // 5)
print(type(10 // 5))

# Yorum satırı

string_1 = "Ali"

print(type(string_1))

print(string_1[0])


number = 10.6

print(number)
print(type(number))

print(int(number))
print(type(int(number)))

print(str(number))
print(type(str(number)))


number = 0

print(bool(number))
print(bool(1))
print(bool(-1))

text = ""
print(bool(text))

text = " "
print(bool(text))


number = 0.0
print(bool(number))


number = 31.0
print(bool(number))


number_1 = 5
number_2 = 10
number_3 = 15

print(number_1, number_2, number_3)

print(number_1, number_2, number_3, sep="+")
print(number_1, number_2, number_3, sep="\n")
print(number_1, number_2, number_3, sep="\t")


print(number_1, number_2, number_3, sep=" + ", end=" = ")





#print("----------------------")
#name = input("Please enter your name? ")

#print(name)
#print((type(name)))



number = 10

#print("----------------------")
#input_1 = input("Please enter number? ")

#print(number + int(input_1))
#print((type(name)))


sample_string = "Hello World"

print(sample_string[2])
print(sample_string[-2])

print(sample_string[0:3])
print(sample_string[0:-2])


#num1 = int(input("Enter integer"))

#print(num1)
#print(type(num1))




#num1 = int(input("Enter integer 1: "))
#num2 = int(input("Enter integer 2: "))

#print("Sum: " + str(num1+num2))
#print("Subs: " + str(num1-num2))
#print("Mulpt: " + str(num1*num2))
#print("Division: ", num1/num2)
#print("Power: ", num1 ** num2)
#print("Mod: ", num1 % num2)



# if conditions


#number = int(input("Enter integer: "))

if number == 0:
    print("Number is 0")
if number > 0:
    print("Number is positive")
if number < 0:
    print("Number is negateive")


if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negateive")
else:
    print("Number is 0")

if bool(number):
    print("Number is equal to zero")

if number > 5 and number < 8:
    print("Number between 5, 8")

if number > 5:
    if number < 8:
        print("Number between 5, 8")

if 5 > number > 8:
    print("Number between 5, 8")


list_1 = []
list_2 = []
list_3 = list_1


if list_1 == list_2:
    print("True")
else:
    print("False")

if list_1 is list_2:
    print("True")
else:
    print("False")

if list_1 is list_3:
    print("True")
else:
    print("False")


list_3 = list_1 + list_2

if list_1 is list_3:
    print("True")
else:
    print("False")



number = 5
print(number)

number = number + 5
number += 5
number -= 5
number *= 5
number /= 5


text = "Ali"

if "i" in text:
    print("text contains i")
else:
    print("text contains not i")

if "z" in text:
    print("text contains z")
else:
    print("text contains not z")

number = 0
alpabeth = "abcdefgh"

for chars in alpabeth:
    print(chars, end="-")
    number += 1
    print(number, end="\t")

print("\n")
for i in range(0, 10):
    print(i, end=" ")


print("\n")
for i in range(5, 10):
    print(i, end=" ")


print("\n")

for number in range(10):
    print(number, end=" ")

print(number)

for number in range(1,10,2):
    print(number, end=" ")


print("\n")

number = 0
while number < 10:
    print(number, end=" ")
    number += 1




number = 0
while number < 30:
    number += 1
    print(number, end=" ")
    if number % 10 == 0:
        print("\n")


for number in range(1,31):
    print(number, end=" ")
    if number % 10 == 0:
        print("\n")


number = 0
while True:
    number += 1
    print(number)
    if number == 2:
        break


print("\n")

for number in range(10,0,-2):
    print(number)






input_1 = input("Kelime girin:")

removedChars = ""


for letter in input_1:
    if letter.isalnum():
        removedChars = removedChars + letter

backwards = removedChars[::-1]

print(input_1.lower())

print(backwards.lower())
print(removedChars.lower())


if removedChars.lower() == backwards.lower():
    print("Palindrom")
else:
    print("Palindrom değil")

