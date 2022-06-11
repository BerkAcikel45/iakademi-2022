import pymongo
from pymongo import MongoClient

def get_database():
    connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.0"

    client = MongoClient(connection_string)
    return client["nutri"]

def insert_data():
    item_1 = {
        "food": "5 olives",
        "calories": 300
    }
    item_2 = {
        "food": "avacado",
        "calories": 450
    }
    item_3 = {
        "food": "4 walnuts",
        "calories": 250
    }
    item_4 = {
        "food": "10 almonds",
        "calories": 550
    }
    item_5 = {
        "food": "chocolade",
        "calories": 650
    }

    dbname = get_database()
    dbname.fat.insert_many([item_1, item_2, item_3, item_4, item_5])


insert_data()

