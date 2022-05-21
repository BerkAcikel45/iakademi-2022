numbers = [1, 1, 2, 3, 4, 5]
set_numbers = set(numbers)

print(set_numbers)

set_List = {1, 5, 3, 2}

set_List_2 = {1.0, 2, "Hello", (1, 2, 3)}
print(set_List_2)

mySet = set()
print(type(mySet))
print(mySet)

mySet = {1, 2, 3}

mySet.add("Hello")
mySet.add(5)
mySet.add(3)
print(mySet)

mySet.update([1, 12, 13])
print(mySet)

mySet.discard(12)
print(mySet)

mySet.remove(5)
print(mySet)

{}.get("a", [])

mySet.discard("asdas")
# mySet.remove("asdas")

mySet.pop()

set_alf = set("HelloWorld")
a = list("Heff")

print(set_alf)
print(a)

set_alf.clear()
print(set_alf)

B = {100, 1, 2, 3, 4}
A = {100, 10, 20, 30, 4}

print("setList after Union: {setlist}".format(setlist=A | B))
print("setList after Union: {setlist}".format(setlist=A.union(B)))
print("setList after Union: {setlist}".format(setlist=B.union(A)))

print("setList after Intersection: {setlist}".format(setlist=A & B))
print("setList after Intersection: {setlist}".format(setlist=A.intersection(B)))

print("setList after Difference: {setlist}".format(setlist=A - B))
print("setList after Difference: {setlist}".format(setlist=A.difference(B)))

numberList = [1, 2, 3, 4]
numberList.append(5)

numberList_2 = []
for i in numberList:
    numberList_2.append(i)

numberlist_3 = [i * 2 for i in numberList]

print(numberlist_3)

numberList = [(1, 2), (4, 5), (8, 9)]
numberList2 = [x * y for x, y in numberList]

print(numberList2)

numberList = [1, 2, 3, 4, 5, 6, 7, 8]
numberList2 = [i for i in numberList if not (i == 3 or i == 8)]

numberList3 = [i for i in numberList if (i != 3 and i != 8)]
print(numberList3)

print(numberList2)

# while True:
#     try:
#         number = int(input("Enter integer"))
#         break
#     except ValueError:
#         print("Invalid input")

# while True:
#     try:
#         age = int(input("Enter your age: "))
#         try:
#             0 / 5
#         except ZeroDivisionError:
#             pass
#     except ValueError:
#         print("Invalid input")
#     else:
#         print(f"your age is {age}")
#     finally:
#         print("Loop")


customers = [{"name": "berk", "password": "aaa", "account": 1500},
             {"name": "ALİ", "password": "bbb", "account": 2000}
 ]







# while True:
#     name = input("Enter Name")
#     password = input("Enter Password")

    #customerValidation(name, password)

# Ürünler
# Filtre Kahve: 25
# Türk Kahvesi: 20
# Çay: 10
# Su: 10

sonuc = {}
total = 0
while True:
    siparis = input("Ne istersiniz ? 1: Filtre Kahve, 2: Türk Kahvesi, 3: Çay, 4: Su çıkış için q ya basınız")
    if siparis == "q":
        result = ""
        for k, v in sonuc.items():
            result += str(v.get("adet")) + "X" + k + " fiyatı:" + str(v.get("sum")) + " toplam: "
        print(result + " total: "+ str(total))

    adet = input("Adet giriniz")

    if siparis == "1":
        sonuc["filtre kahve"] = {"adet": int(adet), "sum": 25 * int(adet)}
        total += 25 * int(adet)
    elif siparis == "2":
        sonuc["türk kahvesi"] = {"adet": int(adet), "sum": 20 * int(adet)}
        total += 25 * int(adet)

    elif siparis == "3":
        sonuc["çay"] = {"adet": int(adet), "sum": 10 * int(adet)}
        total += 25 * int(adet)

    elif siparis == "4":
        sonuc["su"] = {"adet": int(adet), "sum": 10 * int(adet)}
        total += 25 * int(adet)

