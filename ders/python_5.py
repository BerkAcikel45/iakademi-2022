#
# bannedWords = ["salak", "aptal"]
# sentence = input("Enter words")
# words = sentence.split(" ")
# output = ""
# for word in words:
#     if word in bannedWords:
#         output += " . "
#
#         output.replace("", ".")
#     else:
#         output += " " + word
#
# print(output)
#
#
from typing import List


def sum(number_1, number_2):
      return number_1 + number_2

# def subs(number_1, number_2):
#      return number_1 - number_2
#
# def division(number_1, number_2):
#      return  number_1 / number_2
#
# def multiply(number_1, number_2):
#     return  number_1 * number_2
#
# while True:
#     choose = input("Choose +, -, /, * or -1 for exit")
#     if choose == "-1":
#         break
#
#     num_1 = int(input("Enter first integer: "))
#     num_2 = int(input("Enter second integer: "))
#     if choose == "+":
#         print(sum(num_1, num_2))
#     elif choose == "-":
#         print(subs(num_1, num_2))
#     elif choose == "/":
#         print(division(num_1, num_2))
#     elif choose == "*":
#         print(multiply(num_1, num_2))

def getNumbers():
    numbers = []
    while True:
        try:
            number = int(input("Enter number"))
            numbers.append(number)
        except ValueError:
            break
    return numbers

def addition(numbers: List[int]):
    result = 0
    for number in numbers:
        result += number
    return result

def selectOperation(numbers):
    operation = input("Please select an operation \n + for addition \n - for substraction \n * \ /")

    if operation == "+":
        print(addition(numbers))



selectOperation(getNumbers())