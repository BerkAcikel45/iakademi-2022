import time
from time import sleep

import requests

users = []
final = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daily_expense = {}
daily_expenses = []
sum_ = 0


class Expense:
    def __init__(self, entertainment, clothing, fuel, food):
        self.entertainment = entertainment
        self.clothing = clothing
        self.fuel = fuel
        self.food = food

    def set_daily_expense(self):
        return self.entertainment + self.clothing + self.fuel + self.food

    def set_weekly_expense(self):
        pass


class Balance(Expense):
    def __init__(self, entertainment, clothing, fuel, food, earning, sum_expense):
        super(Balance, self).__init__(entertainment, clothing, fuel, food)
        self.earning = earning
        self.sum_expense = sum_expense

    def set_balance(self):
        return self.earning - self.sum_expense


def temperature():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=6d8e4d350debeb87cc733e79258482ca&units=metric")
    data = response.json()
    main = data.get('main')
    temperature = main.get('temp')
    if __name__ == '__main__':
        return temperature


def weather():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=6d8e4d350debeb87cc733e79258482ca&units=metric")
    data = response.json()
    w1 = data.get('weather')
    w2 = w1[0]
    weather = w2.get('description')
    if __name__ == '__main__':
        return weather

while True:
    choice = input(
        "1- New User\n2-I have a username\n3-My weekly expense\n4-Write 'q' for exit\nChoose one:")
    if choice == "q":
        print("exiting...")
        time.sleep(3)
        break
    elif choice == "1":
        user1 = input("enter Username")
        users.append(user1)
        print(f"welcome {user1}")
        print(f"today it's {temperature()} ℃ and {weather()}")
        print(users)
    elif choice == "2":
        member = input("enter your username")
        for i in users:
            if i == member:
                earning_1 = int(input(f"Enter your weekly earning:"))
                for a in range(6):
                    ent_1 = int(input(f"Enter {days[a]}'s entertainment expense:"))
                    clo_1 = int(input(f"Enter {days[a]}'s clothing expense:"))
                    fuel_1 = int(input(f"Enter {days[a]}'s fuel expense:"))
                    food_1 = int(input(f"Enter {days[a]}'s food expense:"))
                    dict_1 = {
                        "entertainment": ent_1,
                        "clothing": clo_1,
                        "fuel": fuel_1,
                        "food": food_1
                    }
                    dict_2 = {
                        f"{days[a]}": dict_1
                    }
                    final.append(dict_2)
                    exp_1 = Expense(ent_1, clo_1, fuel_1, food_1)
                    sum_ += exp_1.set_daily_expense()
                    bal_1 = Balance(ent_1, clo_1, fuel_1, food_1, earning_1, sum_)
                    print(f"you spent{exp_1.set_daily_expense()} on {days[a]}")
                    print(f"your weekly balance is {bal_1.set_balance()} ")

            else:
                print("enter a valid username")
        dict_3 = {
            "name": member,
            "member_info": final
        }
        print(dict_3)
    elif choice == "3":
        member = input("enter your username")
        for a in dict_3.items():
            if dict_3.get("name") == member:
                print(dict_3)
            else:
                print("enter a valid username")
