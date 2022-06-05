import pymongo
from pymongo import MongoClient


def get_database():
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.0"

    client = MongoClient(connection_string)

    return client["iakademi"]



def insert_data():
    item_1 = {
        "name": "Berk",
        "surname": "Açıkel",
        "title": "Muh",
        "School": "Yasar",
        "Age": 25,
    }
    item_2 = {
        "name": "Ali",
        "surname": "Veli",
        "title": "bb",
        "School": "aaa",
        "Age": 22,
    }

    dbname = get_database()
    dbname.test.insert_many([item_1, item_2])


#insert_data()

dbname = get_database()
collection_name = dbname["test"]

details = collection_name.find()

for data in details:
    print(data)