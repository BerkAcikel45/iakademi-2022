#
#
# sentence = input("Enter senctence")
# char = input("Enter char")
#
# def solution_1(sentence, char):
#     sentence_len = len(sentence)
#
#     for i in range(sentence_len):
#         if char == sentence[i]:
#             print(f"Index number: {i + 1}, ")
#             break
#
# solution_1(sentence, char)
#
# def solution_2(sentence, char):
#     counter = 0
#     for character in sentence:
#         counter += 1
#         if char == character:
#             print(f"Index number: {counter}, ")
#
# solution_2(sentence, char)
#
#
# def solution_3(sentence, char):
#     index = sentence.index(char)
#     print(f"Index number: {index + 1 }")
#
# solution_3(sentence, char)





#
# # TUPLE
#
# tuple_1 = (1, 2, 4)
# print(type(tuple_1))
# print(tuple_1)
#
# tuple_2 = (1,)
#
# print(tuple_2)
# print(type(tuple_2))
#
#
# evenNumbers = []
# for i in range(10):
#     if i % 2 == 0:
#         evenNumbers.append(i)
#
# print(evenNumbers)
#
#
# evenNumbers = [i for i in range(10) if i % 2 == 0]
#
# print(evenNumbers)
#
#
# evenNumbers = [i for i in range(2, 100001, 2)]
# tupleEvenNumber = tuple(evenNumbers)
#
#
# import sys
#
# print(f"Even numbers list:  {sys.getsizeof(evenNumbers)}")
# print(f"Even numbers tuple:  {sys.getsizeof(tupleEvenNumber)}")
#
# import timeit
#
# print("List time: ", timeit.timeit(stmt="numbers = [1,2,3,4,5]"))
# print("Tuple time: ", timeit.timeit(stmt="numbers = (1,2,3,4,5)"))
#
# tuple_1 = (1, 2, 4)
# print(tuple_1[1])
# print(tuple_1[-1])
# print(tuple_1[1:])
# print(tuple_1.index(4))
# print(tuple_1.count(2))
# del tuple_1
# a = 5
# del a
#
#
#
# # Dictionary
#
# dict_1 = {}
#
# dict_1 = dict()
#
# print(type(dict_1))
#
#
# dict_1 = {
#     0: {
#         "Name": "Berk",
#         "Age": 25,
#         "School": "AAA"
#     },
#     1: {
#         "Name": "Ali",
#         "Age": 25,
#         "School": "AAA"
#     }
# }
#

#dict_1 = dict(name="Berk", Age=25, School="AAA")

#
# print(dict_1[0])
# print(dict_1[0]["Name"])
# print(dict_1[0]["School"])
#
# dict_1[0]["Name"] = "Veli"
#
# print(dict_1[0])


#
# dict_2 = {
#     "Name": "Berk",
#     "Surname": "Açıkel"
# }
#
#
# print(dict_2["Name"])
# print((dict_2.get("Name")))
# print(dict_2.get("Surname"))
# print(dict_2.pop("Name"))
# print(dict_2)
#
#
# a = dict_2.popitem()
#
# print(dict_2)
#
#
# dict_3 = {"Age": 15, "Name": "Berk"}
# print(dict_3.clear())
# print(dict_3)
#
#
# dict_3 = {"Age": 15, "Name": "Berk"}
#
# print(dict_3.items())
#
# for key, value in dict_3.items():
#     print(key)
#     print(value)
#
#
# for a in dict_3.items():
#     print(a)
#
# print(dict_3.values())
#
# print(dict_3.keys())
#
#

# list_1 = []
# while True:
#     name = input("Enter Name: ")
#     last_name = input("Enter Last name: ")
#     age = input("Enter Age: ")
#
#
#     dict_1 = {
#         "name": name,
#         "last_name": last_name,
#         "age": age
#     }
#     list_1.append(dict_1)
#
#     exit_ = input("Exit for -1 ")
#     if exit_ == "-1":
#         break
#
# print(list_1)
# name = input("Enter name for information ")

# for data in list_1:
#
#     if data.get("name") != name:
#         continue
#     else:
#         print(f"All information is: {data}")
#         break

# counter = 0
# len_list_1 = len(list_1)
# for data in list_1:
#
#     if data.get("name") != name:
#         continue
#     else:
#         print(f"All information is: {data}")
#
#     if counter == len_list_1:
#         print(f"{name} not exists....")
#     counter += 1
#
#

number = int(input("Enter integer"))
even = []
odd = []
for i in range(number + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)