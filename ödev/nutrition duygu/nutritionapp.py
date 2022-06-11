import pymongo
from pymongo import MongoClient

food_types = ["protein", "carb", "fat"]


def get_database():
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.0"

    client = MongoClient(connection_string)
    return client["nutri"]


class DailyCalories:
    def __init__(self, protein, carb, fat):
        self.protein = protein
        self.carb = carb
        self.fat = fat

    def calculate_daily_calories(self):
        return self.protein + self.carb + self.fat


class Measurement:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def find_daily_calories_to_lose_weight(self):
        if 150 < self.height < 170:
            if 40 < self.weight < 60:
                return 2000
            elif 61 < self.weight < 80:
                return 1800
            elif 81 < self.weight < 100:
                return 1600
            elif self.weight > 100:
                return 1400
        elif 171 < self.height < 190:
            if 40 < self.weight < 60:
                return 2200
            elif 61 < self.weight < 80:
                return 2000
            elif 81 < self.weight < 100:
                return 1800
            elif self.weight > 100:
                return 1600
        elif self.height >= 190:
            if 40 < self.weight < 60:
                return 2400
            elif 61 < self.weight < 80:
                return 2200
            elif 81 < self.weight < 100:
                return 2000
            elif self.weight > 100:
                return 1800


class AddUser(Measurement):
    def __init__(self, weight, height, username):
        super(AddUser, self).__init__(weight, height)
        self.username = username

    def insert_user(self,):
            item_1 = {
                "name": self.username,
                "height": self.height,
                "weight": self.weight,
            }
            dbname = get_database()
            dbname.users.insert_many([item_1])


user1 = input("Enter your name")
weight1 = int(input("Enter your weight"))
height1 = int(input("Enter your height"))
info = AddUser(username=user1, weight=weight1, height=height1)

AddUser.insert_user(info)


m1 = Measurement(weight1, height1)

dailyCalories = Measurement.find_daily_calories_to_lose_weight(m1)
print(f"Your will have daily {dailyCalories} calories")
print(dailyCalories)

dbname = get_database()

collection_name1 = dbname["protein"]
collection_name2 = dbname["carb"]
collection_name3 = dbname["fat"]

details = collection_name2.find()

for data in details:
    print(data)

# while dailyCalories > 0:
#     for food in food_types:
#         if food == collection_name1:
#             a = dailyCalories - collection_name1.find("calories")
#             print(a)



