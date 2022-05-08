
#wwwbbc

alphabet = "abcdefghlmnoprklüpoızx"
output = ""


#text = input("Enter:")

#print(text.count("a"))
#for char in alphabet:
#    count = text.count(char)

#    if char in text:
#        output += char + str(count)

#print(output)


index = 1
while index <= 5:
    print(index)
    index = index + 1



import random

randomNumber = random.randint(1, 5)


guessCount = 0
guessLimit = 3

print("--------")
print(randomNumber)

#while guessCount < guessLimit:
#    guess = int(input("Enter integer: "))
#    guessCount += 1
#    if guess == randomNumber:
#        print("You won")
#        break
#    else:
#        print("Try Again" + " you have try count " + str(3 - guessCount))
#else:
#    print("You failed")



number = [64, 20, 11, 55, 88, 123, 444, 90]

#for i in number:
#    if i % 2 == 0:
#        print(str(i)+ " çift sayıdır")
#        print(f"{str(i)} çift sayıdır")
#    else:
#        print(str(i) + " tek sayıdır")


#for outterIndex in range(1,6):
#    for innerIndex in range(1,6):
#        print(outterIndex*innerIndex, end=" ")


#for outterIndex in range(1, 6):
#    if outterIndex == 3:
#        continue
#    for innerIndex in range(1, 6):
#        if innerIndex == 3:
#            continue
#        print(f"{outterIndex*innerIndex:4}", end="")


#anonation
def calculateSum(number_1: int, number_2: int) -> int:
    return number_1 + number_2

def calculateSubs(number_1: int, number_2: int) -> int:
    return number_1 - number_2


sum_1: int = calculateSum(4, 4)
sum_2: int = calculateSum(8, 14)

subs_1 = calculateSubs(4, 4)
subs_2 = calculateSubs(8, 4)

print(sum_1)
print(sum_2)

print(subs_1)
print(subs_2)


def validateEmail(email):
    print(email.count("."))
    if email.count("@") != 1 or email.count(".") != 1:
        return False
    if len(email) > 20:
        return False
    return True


print(validateEmail("berk....@gmail.com"))

print(validateEmail("berk@gmail.com"))



