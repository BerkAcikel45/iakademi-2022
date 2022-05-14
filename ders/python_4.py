import random


randomNumbers = []
for i in range(10):
    randomNumber = random.randint(1, 10)
    if randomNumber in randomNumbers:
        print(f"{randomNumber} is already exists")
    else:
        randomNumbers.append(randomNumber)


print(randomNumbers)

randomNumbers = []
index = 0


list_1 = []


while True:
    if index == 10:
        break

    randomNumber = random.randint(1, 10)
    if randomNumber in randomNumbers:
        print(f"{randomNumber} is already exists")
    else:
        randomNumbers.append(randomNumber)
        index += 1

print(randomNumbers)


numbers = []
for i in range(5):
    random_num = random.randint(1, 100)
    numbers.append(random_num)

print(numbers)
while True:
    if len(numbers) == 3:
        break

    user_value = input("Enter integer: ")
    if int(user_value) in numbers:
        print(f"{user_value} deleted")
        numbers.remove(int(user_value))
        print(numbers)

print(numbers)

numbers = []
index = 0
while True:
    if len(numbers) == 3:
        break

    randomNumber = random.randint(1, 10)
    if index < 5:
        numbers.append(randomNumber)

    index += 1

    user_value = input("Enter integer: ")
    if int(user_value) in numbers:
        print(f"{user_value} deleted")
        numbers.remove(int(user_value))
        print(numbers)


"".split(" ")

"berk açıkel".split(" ")






