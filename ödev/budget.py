import requests


class App:
    days = ["Monday", "Tuesday"]

    users = {}  # attributes for each user; dictionary
    USERS = []  # contains usernames to check for a duplicate username

    daily_costs = []  # money spent per day
    total_cost = []  # sum of daily_cost's elements

    food_costs = []
    entertaining_costs = []
    clothing_costs = []
    fuel_costs = []

    def __init__(self, balance, food, entertainment, clothing, fuel):
        self.food = food
        self.balance = balance
        self.entertainment = entertainment
        self.clothing = clothing
        self.fuel = fuel

    def calculate_money_spent(self):
        return self.food + self.entertainment + self.clothing + self.fuel

    def fetch_weather_data():
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=izmir&appid=8af3aba99edd9fb699076f610994383c&units=metric")
        data = response.json()
        return data.get("name") + " " + str(data.get("main").get("temp"))


while True:
    # initial balance and a username value are required for execution
    get_username = input("Choose a username: ").lower()

    if get_username not in App.USERS and get_username.isalnum() and get_username != "q":
        App.USERS.append(get_username)
        get_balance = int(input("Initial Balance: "))

        for day in App.days:
            print("------------------------------------------------------")
            print(f"{day}")
            get_food = int(input("How much money do you spend on food? "))
            get_entertainment = int(
                input("How much money do you spend on entertainment? "))
            get_clothing = int(
                input("How much money do you spend on clothing? "))
            get_fuel = int(input("How much money do you spend on fuel? "))

            user_1 = App(get_balance, get_food, get_entertainment,
                         get_clothing, get_fuel)

            App.users.update({get_username: {
                'balance': get_balance,
                'food': get_food,
                'entertainment': get_entertainment,
                'clothing': get_clothing,
                'fuel': get_fuel
            }})

            money_spent = user_1.calculate_money_spent()
            remaining_balance = App.users[get_username]['balance'] - money_spent
            App.users[get_username].update({'balance': remaining_balance})

            App.food_costs.append(get_food)
            App.entertaining_costs.append(get_entertainment)
            App.clothing_costs.append(get_clothing)
            App.fuel_costs.append(get_fuel)

            App.total_cost.append(money_spent)

            App.daily_costs.append(
                f"{get_username} spent ₺{money_spent} on {day} - {App.fetch_weather_data()}°C")

        print("------------------------------------------------------")
        print("STATS")
        print(f"Spent {sum(App.food_costs)} on food.\nSpent {sum(App.entertaining_costs)} on entertainment.\nSpent {sum(App.clothing_costs)} on clothing.\nSpent {sum(App.fuel_costs)} on fuel.")

        print("------------------------------------------------------")
        print(f"Initial balance: {get_balance}")
        print(
            f"Current balance: {get_balance - sum(App.total_cost)}")
        print(f"Total spent: {sum(App.total_cost)}")
        print("------------------------------------------------------")
        for daily_cost in App.daily_costs:
            print(daily_cost)
        print("------------------------------------------------------")

        App.food_costs.clear()
        App.entertaining_costs.clear()
        App.clothing_costs.clear()
        App.fuel_costs.clear()

    # if user wants to quit the program
    elif get_username == "q":
        break
    else:
        print("This username is already taken or contains invalid characters.")
