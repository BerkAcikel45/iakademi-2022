
# BUDGET APP:
# CLASS YAPISI
# FOOD, ENTERTAINMENT, CLOTHING, FUEL

# USER-1 --> 1000 -> 100 ENTERTAINMENT, 300 CLOTHING, 500 FUEL, 200 FOOD -
# MONDAY --> ENTERTAINMENT 40 --> 30 derece
# TUESDAY --> ENTERTAINMENT 60, 100 CLOTHING  --> 30 derece
# WEDNESDAY --> 200 FOOD  --> 30 derece
# THURSDAY --> 200 CLOTHING  --> 30 derece
# FRIDAY -->  500 FUEL --> 30 derece
# - 100

# USER-2 --> 2000
# + 2000

# WEATHER APP



from time import sleep

import requests



a = {"a": {'a': 1, }}
print(a["a"])


class Converter:
    url = "http://data.fixer.io/api/latest?access_key=3eaf33d4a77e6bd74182ebc4c486a"

    def __init__(self, from_currency, to_currency, amount):
        self.amount = amount
        result = requests.get(self.url)

        if result.status_code > 200:
            print("Server Down")
            sleep(10)
            result = requests.get(self.url)

        self.rates = result.json()["rates"]
        self.from_currency = self.rates[from_currency]
        self.to_currency = self.rates[to_currency]

    def convert(self):
        currency_1 = self.to_currency / self.from_currency
        return self.amount * currency_1

from_currency = input("Enter From: ")
to_currency = input("Enter To: ")
amount = input("Enter Amount:")


c1 = Converter(from_currency, to_currency, amount)



# BUDGET APP:
# CLASS YAPISI
# FOOD, ENTERTAINMENT, CLOTHING, FUEL

# USER-1 --> 1000 -> 100 ENTERTAINMENT, 300 CLOTHING, 500 FUEL, 200 FOOD -
# MONDAY --> ENTERTAINMENT 40 --> 30 derece
# TUESDAY --> ENTERTAINMENT 60, 100 CLOTHING  --> 30 derece
# WEDNESDAY --> 200 FOOD  --> 30 derece
# THURSDAY --> 200 CLOTHING  --> 30 derece
# FRIDAY -->  500 FUEL --> 30 derece
# - 100

# USER-2 --> 2000
# + 2000

# WEATHER APP




